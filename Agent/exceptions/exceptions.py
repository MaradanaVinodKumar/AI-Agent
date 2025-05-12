class NotFoundError(Exception):
    def __init__(self, name: str):
        self.name = name


class BadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message


class InternalServerError(Exception):
    def __init__(self, message: str):
        self.message = message

class UnauthorizedError(Exception):
    def __init__(self, message: str):
        self.message = message