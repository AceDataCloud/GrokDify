from __future__ import annotations

from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.acedata_client import AceDataGrokClient, AceDataGrokError


class GrokProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        token = credentials.get("acedata_bearer_token")
        if not isinstance(token, str) or not token.strip():
            raise ToolProviderCredentialValidationError("Missing `acedata_bearer_token`.")
        try:
            AceDataGrokClient(bearer_token=token).validate()
        except (AceDataGrokError, ValueError):
            raise ToolProviderCredentialValidationError(
                "Unable to validate the token. Check its service access and network connection."
            ) from None
