### backend/app/apis/prompts.py [coder:save]
```python
from fastapi import APIRouter, HTTPException, Depends
from typing import List
import httpx
import os
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")
EXTERNAL_API_TOKEN = os.getenv("EXTERNAL_API_TOKEN")

@router.get("/external", response_model=List[PromptResponse])
async def list_external_prompts():
    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL_API_URL}/prompt-templates", headers=headers)
        response.raise_for_status()
        external_prompts = response.json()
        return [PromptResponse(title=prompt["title"], description=prompt["description"]) for prompt in external_prompts]

@router.post("/external", response_model=PromptResponse)
async def create_external_prompt(request: CreatePromptRequest):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{EXTERNAL_API_URL}/prompt-templates",
            json=request.dict(),
            headers=headers
        )
        response.raise_for_status()
        created_prompt = response.json()
        return PromptResponse(title=created_prompt["title"], description=created_prompt["description"])
```
[coder:end]