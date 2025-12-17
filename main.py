from fastapi import FastAPI
from pydantic import BaseModel
from backend.master_agent import handle_message


app = FastAPI(title="Agentic AI Retail Prototype")

class UserInput(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
def chat(input: UserInput):
    response = handle_message(input.session_id, input.message)
    return {"response": response}
