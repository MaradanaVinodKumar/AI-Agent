import uuid
from datetime import datetime
from typing import List, Optional

meetings = {} 

def schedule_meeting(title: str, start_time: str, end_time: str, participants: List[str]) -> dict:
    meeting_id = str(uuid.uuid4())
    start = datetime.fromisoformat(start_time)
    end = datetime.fromisoformat(end_time)
    if start >= end:
        raise ValueError("Start time must be before end time")
    
    meetings[meeting_id] = {
        "id": meeting_id,
        "title": title,
        "start_time": start,
        "end_time": end,
        "participants": participants,
        "created_at": datetime.utcnow()
    }
    return meetings[meeting_id]

def cancel_meeting(meeting_id: str) -> bool:
    if meeting_id in meetings:
        del meetings[meeting_id]
        return True
    return False

def list_meetings() -> List[dict]:
    return list(meetings.values())
