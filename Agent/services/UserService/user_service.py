from Agent.services.UserService.i_user_service import IUserService
from Agent.models.models import AgentRequest
from Agent.exceptions.exceptions import NotFoundError
from Agent.services.genai_sevice import process_Agent_Request



class UserService(IUserService):

    def process_agent_request(self,userRequest : AgentRequest,userKey:str) -> dict:
        # Example implementation logic

        if(userKey != "valid_user_key"):
            raise NotFoundError("User not found")
        return process_Agent_Request(userRequest)