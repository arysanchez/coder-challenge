### backend/app/apis/prompts.py [coder:save]
```
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import datetime
from uuid import uuid4
import httpx
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

# Dependency to simulate authentication
def get_current_user(token: str = Depends()):
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return "user-id"

@router.post("/", response_model=Prompt)
async def create_prompt(request: CreatePromptRequest, user_id: str = Depends(get_current_user)):
    new_prompt = Prompt(
        id=str(uuid4()),
        title=request.title,
        description=request.description,
        prompt=request.prompt,
        visibleTo=request.visibleTo,
        visibleToGroups=request.visibleToGroups,
        categories=request.categories,
        createdAt=datetime.utcnow(),
        updatedAt=datetime.utcnow(),
        isOwner=True,
        ownerId=request.ownerId
    )
    prompts_db.append(new_prompt)
    return new_prompt

@router.get("/", response_model=List[PromptResponse])
async def list_prompts():
    return [PromptResponse(title=prompt.title, description=prompt.description) for prompt in prompts_db]

@router.get("/external", response_model=List[PromptResponse])
async def list_external_prompts():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dev.flow.ciandt.com/channels-service/v1/prompt-templates")
        response.raise_for_status()
        external_prompts = response.json()
        return [PromptResponse(title=prompt["title"], description=prompt["description"]) for prompt in external_prompts]

@router.post("/external", response_model=PromptResponse)
async def create_external_prompt(request: CreatePromptRequest, token: str = Depends(get_current_user)):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://dev.flow.ciandt.com/channels-service/v1/prompt-templates",
            json=request.dict(),
            headers=headers
        )
        response.raise_for_status()
        created_prompt = response.json()
        return PromptResponse(title=created_prompt["title"], description=created_prompt["description"])
```
[coder:end]