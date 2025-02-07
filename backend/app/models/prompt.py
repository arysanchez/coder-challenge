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
    createdAt: datetime
    updatedAt: datetime
    isOwner: bool
    ownerId: str

class CreatePromptRequest(BaseModel):
    title: str
    description: str
    prompt: str
    visibleTo: str
    visibleToGroups: List[str]
    categories: List[str]
    ownerId: str

class PromptResponse(BaseModel):
    id: str
    title: str
    description: str

# In-memory storage for prompts
prompts_db = []