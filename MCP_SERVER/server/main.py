from tools.meetingScheduler import meeting_scheduler
from tools.taskManager import task_manager
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ProductivityServer")

@mcp.tool()
def add_task(title: str, description: str = None, due_date: str = None) -> dict:
    return task_manager.add_task(title, description, due_date)

@mcp.tool()
def delete_task(task_id: str) -> bool:
    return task_manager.delete_task(task_id)

@mcp.tool()
def list_tasks() -> list:
    return task_manager.list_tasks()

@mcp.tool()
def complete_task(task_id: str) -> bool:
    return task_manager.complete_task(task_id)

@mcp.tool()
def schedule_meeting(title: str, start_time: str, end_time: str, participants: list) -> dict:
    return meeting_scheduler.schedule_meeting(title, start_time, end_time, participants)

@mcp.tool()
def cancel_meeting(meeting_id: str) -> bool:
    return meeting_scheduler.cancel_meeting(meeting_id)

@mcp.tool()
def list_meetings() -> list:
    return meeting_scheduler.list_meetings()

if __name__ == "__main__":
    print("MCP server is running....")
    mcp.run(transport="stdio")

# if __name__ == "__main__":
#     print("MCP server is running....")
#     mcp.run(transport="http")
