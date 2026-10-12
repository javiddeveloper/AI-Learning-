class LLMError(Exception):
    """Base class for provider-independent LLM failures."""


class LLMRateLimitError(LLMError):
    """The provider rejected the request because of rate limiting or quota."""


class LLMTimeoutError(LLMError):
    """The provider request timed out."""


class LLMAuthenticationError(LLMError):
    """The provider rejected its credentials."""


class LLMProviderError(LLMError):
    """The provider failed for another reason."""
