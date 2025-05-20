from abc import ABC, abstractmethod
from Agent.models.models import AgentRequest

class IUserService(ABC):

    @abstractmethod
    def process_agent_request(self,userRequest : AgentRequest,userKey:str) -> dict:
        pass

    @abstractmethod
    def get_user_token(self,UserEmail : str) -> str:
        pass