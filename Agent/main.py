from fastapi import FastAPI
from Agent.routes import agent
from contextlib import asynccontextmanager
from Agent.exceptions.exceptions import (BadRequestError, InternalServerError, NotFoundError,
    UnauthorizedError)
from Agent.exceptions.error_handlers import not_found_exception_handler, bad_request_exception_handler, internal_server_error_handler, validation_exception_handler, generic_exception_handler,unauthorized_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from Agent.middleware.auth_middleware import AuthMiddleware
from Agent.database.database import Base, engine
import Agent.schemas.DAO

app = FastAPI()

@asynccontextmanager
async def migrateDB(app: FastAPI):
    try:
        print("🚀 Lifespan startup: creating tables if needed.")
        Base.metadata.create_all(engine)
        print("✅ Tables created or already exist.")
    except Exception as e:
        print("❌ Error during DB migration:", str(e))
    yield 
    print("🛑 Lifespan shutdown.")


app = FastAPI(lifespan=migrateDB)

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