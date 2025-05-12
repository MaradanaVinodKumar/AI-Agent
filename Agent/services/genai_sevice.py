from google import genai
from Agent.models.models import AgentRequest

client = genai.Client(api_key="AIzaSyAXdBRzrjq1h13TIfFgQDaNOV9g-6koXq4")

def process_Agent_Request(request_data: AgentRequest):
    try:
        # response = client.models.generate_content(
        #     model="gemini-2.0-flash", 
        #     contents=request_data.command,
        # )
        
        if AskLLM(
            command=request_data.command,
            askLike="Is user asking to add task?"
        ):
            response = client.models.generate_content(
                        model="gemini-2.0-flash", 
                        contents=f"""based on the user command, extract the tasks and return it in a JSON format. 
                        note(dont miss):- If no tasks is found, return an empty JSON object. 
                        User Command: {request_data.command}
                        Example:
                        out put:
                        if tasks is found:
                        [
                            "....."
                        ]
                        
                        if no tasks is found or empty return an empty array object dont give uncessary information just give outpu what i have metioned in the billow:
                        []
                          """
                    )

            if response:
                return {
                    "tasks": response.text.strip(),
                    "status": "success",
                    "message": "Task added successfully."
                }
            else:
                return {
                    "status": "error",
                    "message": "No task found in the response."
                }
            

        response = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=request_data.command,
        )  

        return response.text.strip()
    except Exception as e:
        return {"error": str(e)}
    
def AskLLM(command: str, askLike: str):
    try:
        prompt = f"""
            You are a smart assistant. Analyze the user command and answer strictly with True or False.

            User Command: "{command}"
            Question: "{askLike}"

            Answer with only one word: True or False.
            """
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        reply = response.text.strip().lower()
        if "true" in reply:
            return True
        elif "false" in reply:
            return False
        else:
            return {"error": "Unexpected response: " + reply}
    except Exception as e:
        return {"error": str(e)}