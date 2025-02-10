from pydantic import BaseModel
from typing import List
from datetime import datetime

class PromptVariable(BaseModel):
    name: str
    title: str

class Prompt(BaseModel):
    id: str
    title: str
    description: str
    prompt: str
    variables: List[PromptVariable] = []
    visibleTo: str
    visibleToGroups: List[str]
    categories: List[str]
    isOwner: bool
    ownerId: str

class CreatePromptRequest(BaseModel):
    prompt: str

class PromptResponse(BaseModel):
    title: str
    description: str
    prompt: str
    id: str

# In-memory storage for prompts
prompts_db = []