from .helpers import MessageContent

class Message:
    UserAuthenticated = MessageContent("USER_AUTHENTICATED")
    PasswordChanged = MessageContent("PASSWORD_CHANGED")
    PasswordResetted = MessageContent("PASSWORD_RESET")
    Success = MessageContent("SUCCESS")
    