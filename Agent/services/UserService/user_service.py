from Agent.services.UserService.i_user_service import IUserService
from Agent.models.models import AgentRequest
from Agent.exceptions.exceptions import BadRequestError, NotFoundError
from Agent.services.genai_sevice import process_Agent_Request
from Agent.Utils.Validations.validations import ValidationUtils



class UserService(IUserService):

    def process_agent_request(self,userRequest : AgentRequest,userKey:str) -> dict:
        # Example implementation logic

        if(userKey != "valid_user_key"):
            raise NotFoundError("User not found")
        return process_Agent_Request(userRequest)
    
    def get_user_token(self,UserEmail : str) -> str:
         
         if ValidationUtils.is_valid_email(UserEmail) :
             raise BadRequestError("Not a valid email.")
         
         # need hit the db and fetch the user email details