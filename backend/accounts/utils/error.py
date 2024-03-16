from .helpers import ErrorContent

class Error:
    CreationFailed = ErrorContent("CREATION_FAILED", 1001)
    UpdateFailed = ErrorContent("UPDATE_FAILED", 1002)
    InvalidToken = ErrorContent("INVALID_TOKEN", 1003)
    EmailRequired = ErrorContent("EMAIL_REQUIRED", 1004)
    InvalidEmail = ErrorContent("INVALID_EMAIL", 1005)
    InvalidUser = ErrorContent("INVALID_USER", 1006)
    InvalidLink = ErrorContent("INVALID_LINK", 1007)
    TokenAndUidb64Required = ErrorContent("TOKEN_AND_UIDB64_MISSING", 1008)