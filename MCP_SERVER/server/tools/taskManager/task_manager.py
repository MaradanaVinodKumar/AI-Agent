import uuid
from datetime import datetime
from typing import List, Dict, Optional

tasks = {}
meetings = {} 

def add_task(title: str, description: Optional[str] = None, due_date: Optional[str] = None) -> dict:
    task_id = str(uuid.uuid4())
    due = datetime.fromisoformat(due_date) if due_date else None
    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "description": description,
        "due_date": due,
        "created_at": datetime.utcnow(),
        "completed": False,
    }
    return tasks[task_id]

def delete_task(task_id: str) -> bool:
    if task_id in tasks:
        del tasks[task_id]
        return True
    return False

def list_tasks() -> List[dict]:
    return list(tasks.values())

def complete_task(task_id: str) -> bool:
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        return True
    return False
