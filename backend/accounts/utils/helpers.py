class GenericContent:
    def __init__(self, message, code = 0, type = "message") -> None:
        self.message = message
        self.code = code
        self.type = type

    def __str__(self) -> str:
        return { self.type : {
            "message": self.message,
            "code": self.code if self.type == "error" else 0,
            "status": self.type
        }}

class ErrorContent(GenericContent):
    def __init__(self, message, code) -> None:
        super().__init__(message, code, "error")


class MessageContent(GenericContent):
    def __init__(self, message, code = 0) -> None:
        super().__init__(message, code, "message")
