"""Single-use approval contract for a fully specified LinkedIn mutation.

This module deliberately contains no transport or execution client. Preparing
or confirming an intent cannot publish anything; a caller must separately use
an authorized connector after consuming a permit for the unchanged intent.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from enum import Enum
import hashlib
import json
import secrets
from typing import Callable, Dict, Optional, Tuple

from .url_parser import parse_linkedin_target_url


class ApprovalError(ValueError):
    """Raised when an approval is absent, stale, mismatched, or already used."""


class PublishAction(str, Enum):
    PUBLISH_NOW = "publish-now"
    SCHEDULE = "schedule"


def _normalize_schedule(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ApprovalError("schedule time must be a non-empty ISO 8601 string")
    candidate = value.strip()
    try:
        parsed = datetime.fromisoformat(candidate.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ApprovalError("schedule time must be valid ISO 8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ApprovalError("schedule time must include an explicit UTC offset")
    return parsed.isoformat()


@dataclass(frozen=True)
class PublishIntent:
    action: PublishAction
    linkedin_target: str
    final_content: str
    schedule_time: Optional[str] = None
    media_details: Tuple[str, ...] = ()

    def __post_init__(self) -> None:
        try:
            action = self.action if isinstance(self.action, PublishAction) else PublishAction(self.action)
        except ValueError as exc:
            raise ApprovalError("unsupported publishing action") from exc
        object.__setattr__(self, "action", action)

        target = parse_linkedin_target_url(self.linkedin_target)
        object.__setattr__(self, "linkedin_target", target.canonical)
        if not isinstance(self.final_content, str) or not self.final_content.strip():
            raise ApprovalError("final content must be non-empty")
        if "\x00" in self.final_content:
            raise ApprovalError("final content must not contain null bytes")

        normalized_time = _normalize_schedule(self.schedule_time)
        if action is PublishAction.SCHEDULE and normalized_time is None:
            raise ApprovalError("scheduled actions require an exact time with UTC offset")
        if action is PublishAction.PUBLISH_NOW and normalized_time is not None:
            raise ApprovalError("publish-now actions must not contain a schedule time")
        object.__setattr__(self, "schedule_time", normalized_time)
        object.__setattr__(self, "media_details", tuple(self.media_details))

    def canonical_payload(self) -> str:
        return json.dumps(
            {
                "action": self.action.value,
                "linkedin_target": self.linkedin_target,
                "final_content": self.final_content,
                "schedule_time": self.schedule_time,
                "media_details": list(self.media_details),
            },
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )

    def digest(self) -> str:
        return hashlib.sha256(self.canonical_payload().encode("utf-8")).hexdigest()

    def preview(self) -> str:
        media = "\n".join(f"- {item}" for item in self.media_details) or "- none"
        when = self.schedule_time or "immediately after confirmation"
        return (
            f"Action: {self.action.value}\n"
            f"LinkedIn target: {self.linkedin_target}\n"
            f"Schedule time: {when}\n"
            f"Media/link details:\n{media}\n"
            "Final content (complete):\n"
            f"{self.final_content}"
        )


@dataclass(frozen=True)
class ApprovalRequest:
    token: str
    intent_digest: str
    preview: str
    expires_at: datetime

    @property
    def required_confirmation(self) -> str:
        return f"CONFIRM {self.token}"


@dataclass(frozen=True)
class ApprovalPermit:
    token: str
    intent_digest: str
    expires_at: datetime


class ApprovalGate:
    """Prepare, confirm, and consume exact intents with single-use tokens."""

    def __init__(
        self,
        *,
        ttl: timedelta = timedelta(minutes=15),
        now: Callable[[], datetime] = lambda: datetime.now(timezone.utc),
        token_factory: Callable[[], str] = lambda: secrets.token_urlsafe(24),
    ) -> None:
        if ttl <= timedelta(0):
            raise ValueError("approval TTL must be positive")
        self._ttl = ttl
        self._now = now
        self._token_factory = token_factory
        self._pending: Dict[str, Tuple[str, datetime]] = {}
        self._ready: Dict[str, Tuple[str, datetime]] = {}

    def prepare(self, intent: PublishIntent) -> ApprovalRequest:
        token = self._token_factory()
        if not token or token in self._pending or token in self._ready:
            raise ApprovalError("token factory returned an invalid or duplicate token")
        expires_at = self._now() + self._ttl
        digest = intent.digest()
        self._pending[token] = (digest, expires_at)
        return ApprovalRequest(token, digest, intent.preview(), expires_at)

    def confirm(self, request: ApprovalRequest, response: str) -> ApprovalPermit:
        record = self._pending.get(request.token)
        if record is None or record != (request.intent_digest, request.expires_at):
            raise ApprovalError("approval request is unknown or no longer current")
        if self._now() >= request.expires_at:
            self._pending.pop(request.token, None)
            raise ApprovalError("approval request has expired")
        if response != request.required_confirmation:
            raise ApprovalError("confirmation text does not exactly match the request")
        self._pending.pop(request.token)
        self._ready[request.token] = (request.intent_digest, request.expires_at)
        return ApprovalPermit(request.token, request.intent_digest, request.expires_at)

    def consume(self, permit: ApprovalPermit, intent: PublishIntent) -> None:
        record = self._ready.get(permit.token)
        expected = (permit.intent_digest, permit.expires_at)
        if record is None or record != expected:
            raise ApprovalError("approval permit is unknown or already consumed")
        if self._now() >= permit.expires_at:
            self._ready.pop(permit.token, None)
            raise ApprovalError("approval permit has expired")
        if intent.digest() != permit.intent_digest:
            raise ApprovalError("publishing intent changed after confirmation")
        self._ready.pop(permit.token)
