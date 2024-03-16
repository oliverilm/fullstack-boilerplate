from .error import Error
from .message import Message

class ResponseContent:
    Error = Error()
    Message = Message()

StandardResponse = ResponseContent()