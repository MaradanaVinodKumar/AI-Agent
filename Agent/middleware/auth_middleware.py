from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from starlette.requests import Request
from Agent.exceptions.exceptions import UnauthorizedError

VALID_TOKENS = {"your-valid-token-here"} 

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # auth_header = request.headers.get("Authorization")
        # if not auth_header or not auth_header.startswith("Bearer "):
        
        raise UnauthorizedError("")
            # raise UnauthorizedError("Missing or invalid Authorization header")

        # token = auth_header.removeprefix("Bearer ").strip()
        # if token != "your-valid-token":
        #     raise UnauthorizedError("Invalid token")

        return await call_next(request)