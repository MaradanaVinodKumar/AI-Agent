import fastapi.responses
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from Agent.middleware.JwtServices.jwt_service import JWTService
from starlette.responses import JSONResponse

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.jwt_service = JWTService()

    async def dispatch(self, request: Request, call_next):
        # Allow unauthenticated access to public routes
        public_routes = ["/", "/login"]
        if request.url.path in public_routes:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"detail": "Missing or invalid Authorization header"},
            )

        token = auth_header.split(" ")[1]
        try:
            user_email = self.jwt_service.decode_access_token(token)
            request.state.user = user_email  # Attach email to request
        except ValueError as e:
            return JSONResponse(
                status_code=401,
                content={"detail": str(e)},
            )

        # Token is valid; continue to the next middleware or route handler
        response = await call_next(request)
        return response