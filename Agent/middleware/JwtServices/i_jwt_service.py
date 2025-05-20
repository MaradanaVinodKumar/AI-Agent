from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Optional


class JWTServiceInterface(ABC):
    @abstractmethod
    def create_access_token(self, email: str, expires_delta: Optional[timedelta] = None) -> str:
        pass

    @abstractmethod
    def decode_access_token(self, token: str) -> str:
        pass