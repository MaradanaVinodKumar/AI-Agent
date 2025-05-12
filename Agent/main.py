from fastapi import FastAPI
from Agent.routes import agent
from Agent.exceptions.exceptions import (BadRequestError, InternalServerError, NotFoundError,
    UnauthorizedError)
from Agent.exceptions.error_handlers import not_found_exception_handler, bad_request_exception_handler, internal_server_error_handler, validation_exception_handler, generic_exception_handler,unauthorized_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from Agent.middleware.auth_middleware import AuthMiddleware
app = FastAPI()

# Register routes
app.include_router(agent.router)

app.add_exception_handler(NotFoundError, not_found_exception_handler)
app.add_exception_handler(BadRequestError, bad_request_exception_handler)
app.add_exception_handler(InternalServerError, internal_server_error_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(UnauthorizedError, unauthorized_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# app.add_middleware(AuthMiddleware)

@app.get("/")
def read_root():
    return {"message": "API is working!"}