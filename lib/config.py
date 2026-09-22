"""Safe runtime configuration for draft-only and optional connected modes."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Optional
import os


MCP_ENDPOINT = "https://socialbu.com/mcp"


class ConfigurationError(ValueError):
    """Raised when runtime configuration would weaken the safe default."""


class RuntimeMode(str, Enum):
    DRAFT_ONLY = "draft-only"
    CONNECTED = "connected"


@dataclass(frozen=True)
class RuntimeConfig:
    mode: RuntimeMode = RuntimeMode.DRAFT_ONLY
    mcp_endpoint: Optional[str] = None

    def __post_init__(self) -> None:
        if self.mode is RuntimeMode.DRAFT_ONLY and self.mcp_endpoint is not None:
            raise ConfigurationError("draft-only mode cannot configure an MCP endpoint")
        if self.mode is RuntimeMode.CONNECTED and self.mcp_endpoint != MCP_ENDPOINT:
            raise ConfigurationError("connected mode requires the documented MCP endpoint")

    @property
    def connected_reads_enabled(self) -> bool:
        return self.mode is RuntimeMode.CONNECTED

    @property
    def mutation_authorized(self) -> bool:
        """Configuration never authorizes a publish or schedule mutation."""

        return False


def load_config(environ: Optional[Mapping[str, str]] = None) -> RuntimeConfig:
    """Load configuration without reading or accepting credentials.

    The default remains draft-only even if an endpoint variable is present.
    Connected mode is explicit and only enables discovery/read preparation;
    mutations still require a single-use approval permit.
    """

    values = os.environ if environ is None else environ
    raw_mode = values.get("LINKEDIN_SKILLS_MODE", RuntimeMode.DRAFT_ONLY.value).strip().lower()
    try:
        mode = RuntimeMode(raw_mode)
    except ValueError as exc:
        raise ConfigurationError(f"unsupported LINKEDIN_SKILLS_MODE: {raw_mode!r}") from exc

    if mode is RuntimeMode.DRAFT_ONLY:
        return RuntimeConfig()

    endpoint = values.get("LINKEDIN_SKILLS_MCP_ENDPOINT", "").strip()
    if not endpoint:
        raise ConfigurationError("connected mode requires LINKEDIN_SKILLS_MCP_ENDPOINT")
    return RuntimeConfig(mode=mode, mcp_endpoint=endpoint)
