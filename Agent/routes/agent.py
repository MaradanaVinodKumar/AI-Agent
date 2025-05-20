from fastapi import APIRouter, Depends ,Query,Body,Path, Header, Cookie, Form
from Agent.models.models import AgentRequest
from Agent.services.genai_sevice import process_Agent_Request
from typing import Optional
from Agent.services.UserService.user_service import UserService

router = APIRouter(prefix="/agent", tags=["agent"])

def _UserServices() -> UserService:
    return UserService()

@router.post("/login")
def handle_agent_request(UserKey: str):
    response = _UserServices().GetUserToken(UserKey)
    return response


@router.post("/")
def handle_agent_request(UserKey: str = Query(..., description="API key of the user"),request_data: AgentRequest=Body(...)):
    response = _UserServices().process_agent_request(request_data,UserKey)
    return response


@router.post("/process/{agent_id}")
def handle_agent_request(
    # Path parameter
    agent_id: int = Path(..., description="Agent ID from the URL path"),
    
    # Query parameter
    user_key: str = Query(..., description="User API key"),
    
    # Header
    user_agent: Optional[str] = Header(None, description="User-Agent header"),
    
    # Cookie
    session_id: Optional[str] = Cookie(None, description="Session ID from cookie"),
    
    # JSON Body
    json_body: AgentRequest = Body(...),
    
    # Form Data
    form_field_1: Optional[str] = Form(None),
    form_field_2: Optional[int] = Form(None)
):
    return {
        "agent_id": agent_id,
        "user_key": user_key,
        "user_agent": user_agent,
        "session_id": session_id,
        "json_body": json_body.dict(),
        "form_data": {
            "form_field_1": form_field_1,
            "form_field_2": form_field_2,
        }
    }