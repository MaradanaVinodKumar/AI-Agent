from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR,HTTP_401_UNAUTHORIZED
from Agent.exceptions.exceptions import (BadRequestError, InternalServerError, NotFoundError,
    UnauthorizedError)

async def not_found_exception_handler(request: Request, exc: NotFoundError):
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={"message": f"{exc.name}"}
    )

async def bad_request_exception_handler(request: Request, exc: BadRequestError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"message": exc.message}
    )

async def internal_server_error_handler(request: Request, exc: InternalServerError):
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": exc.message}
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"message": "Request validation error", "errors": exc.errors()},
    )

async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={"message": "Internal server error", "details": str(exc)},
    )

async def unauthorized_exception_handler(request: Request, exc: UnauthorizedError):
    return JSONResponse(
        status_code=401,
        content={"message": f"Unauthorized: {str(exc)}"}
    )