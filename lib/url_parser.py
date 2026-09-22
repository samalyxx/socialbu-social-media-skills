"""Strict parsing and canonicalization for supported LinkedIn URLs."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re
from typing import Collection, Optional
from urllib.parse import parse_qsl, unquote, urlsplit


class LinkedInURLValidationError(ValueError):
    """Raised when a URL is not a supported canonicalizable LinkedIn URL."""


class LinkedInResource(str, Enum):
    PROFILE = "profile"
    ORGANIZATION = "organization"
    SCHOOL = "school"
    POST = "post"
    ARTICLE = "article"


@dataclass(frozen=True)
class LinkedInURL:
    original: str
    canonical: str
    resource: LinkedInResource
    identifier: str


_ALLOWED_HOSTS = {"linkedin.com", "www.linkedin.com", "m.linkedin.com"}
_TRACKING_KEYS = {
    "lipi",
    "midtoken",
    "originalsubdomain",
    "trackingid",
    "trk",
    "utm_campaign",
    "utm_content",
    "utm_medium",
    "utm_source",
    "utm_term",
}
_SLUG = r"[A-Za-z0-9][A-Za-z0-9_-]*"
_PATTERNS = (
    (LinkedInResource.PROFILE, re.compile(rf"^/in/({_SLUG})/?$")),
    (LinkedInResource.ORGANIZATION, re.compile(rf"^/(?:company|showcase)/({_SLUG})/?$")),
    (LinkedInResource.SCHOOL, re.compile(rf"^/school/({_SLUG})/?$")),
    (LinkedInResource.POST, re.compile(rf"^/posts/({_SLUG})/?$")),
    (
        LinkedInResource.POST,
        re.compile(r"^/feed/update/(urn:li:(?:activity|share):[0-9]+)/?$"),
    ),
    (LinkedInResource.ARTICLE, re.compile(rf"^/pulse/({_SLUG})/?$")),
)


def parse_linkedin_url(
    value: str,
    *,
    allowed_resources: Optional[Collection[LinkedInResource]] = None,
) -> LinkedInURL:
    """Validate a supported URL and return a query-free canonical form.

    Only HTTPS URLs on an exact allowlist of LinkedIn hosts are accepted.
    Known tracking parameters are discarded; semantic or redirect-like query
    parameters are rejected so callers cannot mistake a wrapper for a target.
    """

    if not isinstance(value, str) or not value or value != value.strip():
        raise LinkedInURLValidationError("URL must be a non-empty trimmed string")
    if any(ord(character) < 32 for character in value):
        raise LinkedInURLValidationError("URL contains control characters")

    try:
        parsed = urlsplit(value)
        port = parsed.port
    except ValueError as exc:
        raise LinkedInURLValidationError("URL authority is malformed") from exc

    if parsed.scheme.lower() != "https":
        raise LinkedInURLValidationError("URL must use HTTPS")
    if parsed.username is not None or parsed.password is not None:
        raise LinkedInURLValidationError("URL must not contain user information")
    if port not in (None, 443):
        raise LinkedInURLValidationError("URL must not use a custom port")

    host = (parsed.hostname or "").lower().rstrip(".")
    if host not in _ALLOWED_HOSTS:
        raise LinkedInURLValidationError("URL host is not an allowed LinkedIn host")
    if parsed.fragment:
        raise LinkedInURLValidationError("URL fragments are not supported")
    if re.search(r"%(?:2f|5c)", parsed.path, flags=re.IGNORECASE):
        raise LinkedInURLValidationError("Encoded path separators are not supported")

    try:
        path = unquote(parsed.path, errors="strict")
    except UnicodeDecodeError as exc:
        raise LinkedInURLValidationError("URL path contains invalid encoding") from exc
    if "\\" in path or "//" in path:
        raise LinkedInURLValidationError("URL path is malformed")
    if any(segment in {".", ".."} for segment in path.split("/")):
        raise LinkedInURLValidationError("URL path traversal is not supported")

    query = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=False)
    unknown_keys = {key.lower() for key, _ in query} - _TRACKING_KEYS
    if unknown_keys:
        raise LinkedInURLValidationError("URL contains unsupported query parameters")

    selected_resource: Optional[LinkedInResource] = None
    identifier = ""
    for resource, pattern in _PATTERNS:
        match = pattern.fullmatch(path)
        if match:
            selected_resource = resource
            identifier = match.group(1)
            break
    if selected_resource is None:
        raise LinkedInURLValidationError("URL path is not a supported LinkedIn resource")

    if allowed_resources is not None and selected_resource not in set(allowed_resources):
        raise LinkedInURLValidationError("LinkedIn resource type is not allowed here")

    canonical_path = path.rstrip("/")
    return LinkedInURL(
        original=value,
        canonical=f"https://www.linkedin.com{canonical_path}",
        resource=selected_resource,
        identifier=identifier,
    )


def parse_linkedin_target_url(value: str) -> LinkedInURL:
    """Validate a personal or organization target suitable for an intent."""

    return parse_linkedin_url(
        value,
        allowed_resources={
            LinkedInResource.PROFILE,
            LinkedInResource.ORGANIZATION,
            LinkedInResource.SCHOOL,
        },
    )
