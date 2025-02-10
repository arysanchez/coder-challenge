from fastapi import APIRouter, HTTPException, Depends
from typing import List
import httpx
import os
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

EXTERNAL_API_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IkM3Q3V4MXM4V0dfYWNRZE5VLWh3bG1YNGtTV1c5Uzl3dV9oaHVIZVA2TlEiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJmZGUwYzc5Yi1lZjA5LTQ1MGYtYTUwOS0zZDAzMmNlMjFlODUiLCJpc3MiOiJodHRwczovL2NpdGZsb3dkZXZiMmMuYjJjbG9naW4uY29tL2QxZGVhMWU1LThhZWItNDE3ZS1hMWIyLWQ4NDAyZmNmNGE4Zi92Mi4wLyIsImV4cCI6MTczOTI3NDI5MiwibmJmIjoxNzM5MTg3ODkyLCJzdWIiOiIwYzEwMDhhMi01YTIyLTRkODgtYTZlMS1hOGUxYmY0YzEwOGYiLCJlbWFpbCI6ImFyeXNhbmNoZXpAY2lhbmR0LmNvbSIsImdpdmVuX25hbWUiOiJBcnkiLCJmYW1pbHlfbmFtZSI6IkhlbnJpcXVlIGRhIEx1eiBTYW5jaGV6IiwibmFtZSI6IkFyeSBIZW5yaXF1ZSBkYSBMdXogU2FuY2hleiIsImlkcCI6Imdvb2dsZS5jb20iLCJjaGFubmVsIjoicG9ydGFsIiwidGVuYW50IjoiY2l0LWRldiIsInJvbGVzIjoiZmxvd2NvcmUudXNlcixmbG93Y29yZS5hZG1pbixnYWxheHlvcHMudXNlcixjaGF0d2l0aGRvY3MudXNlcixjaGF0d2l0aGRvY3MuYWRtaW4sYmFja2xvZ3JlZmluZXIudXNlciIsInRpZCI6ImQxZGVhMWU1LThhZWItNDE3ZS1hMWIyLWQ4NDAyZmNmNGE4ZiIsImF6cCI6ImZkZTBjNzliLWVmMDktNDUwZi1hNTA5LTNkMDMyY2UyMWU4NSIsInZlciI6IjEuMCIsImlhdCI6MTczOTE4Nzg5Mn0.MPe5JC1Y7e-sBtEsaq9uI4POBXMelvzhVCr-hIL64bMqjrnVDnCTYmIB4gMg4DoXjyQ8pzoA7AYI-otVDKK31Du_7L6pjQXZicuic0CS61I4SZcUcNnx_y_oiy8M5H03hy1Fyfi7_Ou2xIfw2Gm4SiDvyVMo2ZbyQg4AHsfk5LEzZbVlr3d8mbIKFMpa0wiNTxJcRBNInWuZdUND4GGEc5DDKULj1TPDqJ55a0AuU-y9_7WrO-wPy8nsQPrbM3kX43TK5csQYLLRPlBk_TdlJh7I1Ec1tIWWJCO98ipCd261Vf81lquUxKq8t6fp7shWNU5v5qOzpEqrPWVICSwqJA"

@router.get("/list-prompt", response_model=List[PromptResponse])
async def list_external_prompts():
    headers = {
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dev.flow.ciandt.com/channels-service/v1/prompt-templates", headers=headers)
        response.raise_for_status()
        external_prompts = response.json()
        if not isinstance(external_prompts, list):
            raise HTTPException(status_code=500, detail="Invalid response format from external API")
        return [PromptResponse(title=prompt["title"], description=prompt["description"], prompt=prompt["prompt"], id=prompt["id"]) for prompt in external_prompts]



@router.post("/create-prompt", response_model=CreatePromptRequest)
async def create_external_prompt(request: List[CreatePromptRequest]):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    
    # Concatenate prompts
    concatenated_prompt = " ".join([prompt.prompt for prompt in request])
    
    # Send concatenated prompt to LLM
    llm_response = await send_message_to_llm(concatenated_prompt)
    
    # Create new prompt with LLM response
    new_prompt_request = CreatePromptRequest(
        title="Concatenated Prompt",
        description="A prompt created by concatenating multiple prompts.",
        categories="507f191e810c19729de860ea",
        prompt=llm_response["choices"][0]["message"]["content"],
        visibleTo="self",
        visibleToGroups=[]
    )
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://dev.flow.ciandt.com/channels-service/v1/prompt-templates",
                json=new_prompt_request.dict(),
                headers=headers
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error from external API: {exc.response.text}")
        created_prompt = response.json()
        return PromptResponse(title=created_prompt["title"], description=created_prompt["description"], prompt=created_prompt["prompt"])



@router.post("/llm-prompt", response_model=CreatePromptRequest)
async def send_message_to_llm(prompt: str):
    url = "https://dev.flow.ciandt.com/channels-service/v2/chat/messages"
    headers = {
        "Content-Type": "application/json",
        "flowModel": "gpt-4o",
        "flowChannel": "chat-with-docs",
        "flowAgent": "CoderChallenge",
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"  # Use token from environment variable
    }
    payload = {
        "content": [
            {
                "type": "text/plain",
                "value": prompt
            }
        ],
        "model": {
            "name": "gpt4omini",
            "provider": "azure-openai",
            "modelSettings": [
                {
                    "name": "temperature",
                    "value": 0.5
                }
            ]
        },
        "agent": "chat-with-docs",
        "sources": [],
        "connectors": [],
        "operation": "new-question",
        "personaId": "67a6436c0c7895663d38ea92"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error from external API: {exc.response.text}")
        response = await client.post(url, headers=headers, json=payload)
        print("Response Content:", response.content)
        return response.json()