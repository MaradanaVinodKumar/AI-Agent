from Agent.services.UserService.i_user_service import IUserService
from Agent.models.models import AgentRequest
from Agent.exceptions.exceptions import NotFoundError



class UserService(IUserService):

    def process_agent_request(self,userRequest : AgentRequest,userKey:str) -> dict:
        # Example implementation logic

        if(userKey != "valid_user_key"):
            raise NotFoundError("User not found")
        

        response = {
            "status": "success",
            "message": "Agent request processed",
            "data": {
                "agent_id": 123,
                "permissions": ["read", "write"]
            }
        }
        return response