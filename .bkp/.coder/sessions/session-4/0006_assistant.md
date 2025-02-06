O erro `ResponseValidationError` indica que a resposta da rota `list-prompt` não está retornando uma lista válida conforme esperado. Vamos revisar e corrigir a função `list_external_prompts` no arquivo `backend/app/apis/prompts.py` para garantir que ela sempre retorne uma lista válida.

### backend/app/apis/prompts.py [coder:save]
```
from fastapi import APIRouter, HTTPException, Depends
from typing import List
import httpx
import os
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")
EXTERNAL_API_TOKEN = os.getenv("EXTERNAL_API_TOKEN")

@router.get("/list-prompt", response_model=List[PromptResponse])
async def list_external_prompts():
    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL_API_URL}/prompt-templates", headers=headers)
        response.raise_for_status()
        external_prompts = response.json()
        if not isinstance(external_prompts, list):
            raise HTTPException(status_code=500, detail="Invalid response format from external API")
        return [PromptResponse(title=prompt["title"], description=prompt["description"]) for prompt in external_prompts]

@router.post("/create-prompt", response_model=PromptResponse)
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

Essa atualização garante que a função `list_external_prompts` verifica se a resposta da API externa é uma lista antes de tentar processá-la. Se a resposta não for uma lista, uma exceção HTTP 500 será levantada com uma mensagem de erro apropriada. Isso deve resolver o problema de validação da resposta.