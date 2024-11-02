from ninja import Schema

class Response:
    def __init__(self, message, status=200, data=None, errors=None):
        self.message: str = message
        self.status: int = status
        self.data: str = data
        self.errors: str = errors

    def __str__(self) -> str:
        return f"{self.status}: {self.message}"

    def to_dict(self) -> dict[str, str]:
        response_dict: dict[str, str] = {'message': self.message}
        if self.data is not None:
            response_dict['data'] = self.data
        if self.errors is not None:
            response_dict['errors'] = self.errors
        return response_dict

    def to_response(self) -> tuple[int, dict[str, str]]:
        return self.status, self.to_dict()

class IdeaSchema(Schema):
    name: str
    content: str

class MessageResponse(Schema):
    message: str
    data: dict = None

class ErrorResponse(Schema):
    detail: str
    errors: dict = None
