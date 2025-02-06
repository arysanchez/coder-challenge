from fastapi import APIRouter, HTTPException, Depends
from typing import List
import httpx
import os
from ..models.prompt import Prompt, CreatePromptRequest, PromptResponse, prompts_db

router = APIRouter()

EXTERNAL_API_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IkM3Q3V4MXM4V0dfYWNRZE5VLWh3bG1YNGtTV1c5Uzl3dV9oaHVIZVA2TlEiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJmZGUwYzc5Yi1lZjA5LTQ1MGYtYTUwOS0zZDAzMmNlMjFlODUiLCJpc3MiOiJodHRwczovL2NpdGZsb3dkZXZiMmMuYjJjbG9naW4uY29tL2QxZGVhMWU1LThhZWItNDE3ZS1hMWIyLWQ4NDAyZmNmNGE4Zi92Mi4wLyIsImV4cCI6MTczODg4MTk1NCwibmJmIjoxNzM4Nzk1NTU0LCJzdWIiOiIwYzEwMDhhMi01YTIyLTRkODgtYTZlMS1hOGUxYmY0YzEwOGYiLCJlbWFpbCI6ImFyeXNhbmNoZXpAY2lhbmR0LmNvbSIsImdpdmVuX25hbWUiOiJBcnkiLCJmYW1pbHlfbmFtZSI6IkhlbnJpcXVlIGRhIEx1eiBTYW5jaGV6IiwibmFtZSI6IkFyeSBIZW5yaXF1ZSBkYSBMdXogU2FuY2hleiIsImlkcCI6Imdvb2dsZS5jb20iLCJjaGFubmVsIjoicG9ydGFsIiwidGVuYW50IjoiY2l0LWRldiIsInJvbGVzIjoiZmxvd2NvcmUudXNlcixiYWNrbG9ncmVmaW5lci51c2VyLGNoYXR3aXRoZG9jcy51c2VyLGdhbGF4eW9wcy51c2VyIiwidGlkIjoiZDFkZWExZTUtOGFlYi00MTdlLWExYjItZDg0MDJmY2Y0YThmIiwiYXpwIjoiZmRlMGM3OWItZWYwOS00NTBmLWE1MDktM2QwMzJjZTIxZTg1IiwidmVyIjoiMS4wIiwiaWF0IjoxNzM4Nzk1NTU0fQ.REOeDg3AGv4RVDDQ_Kv7WSP1c_0Gbyk4RHiZQwlfppQ59AKbUGQR3vYMACsGzyj0Vp4QNKcDCWpVNGQ8AevG9mHYfjtcNTlqvXqyWyNQ6yYHJxxykbOsIZJsLJ-JI95Mu9GmKpHDMaKKTpkJQ9sX_CZlxrA2OJbklCNtENY5B3jDoYetF_VLByI1zNawG-ij_cOPADAvXndfNzflgcO1t0qukOflV09NS1FnO7ogkUHFpfRy3Ly3sS5f1FFHBVBGiqduDoWEBOLzZdqMHBxL_bYVaFlO1gTyrDLzzn2MsY8gcpOs-CxhJlVPOj1QLeqnXhlLsclyz5HRUnYKsmb8Ew"

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
        return [PromptResponse(title=prompt["title"], description=prompt["description"], prompt=prompt["prompt"]) for prompt in external_prompts]

@router.post("/create-prompt", response_model=PromptResponse)
async def create_external_prompt(request: CreatePromptRequest):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EXTERNAL_API_TOKEN}"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                "https://dev.flow.ciandt.com/channels-service/v1/prompt-templates",
                json=request.dict(),
                headers=headers
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=f"Error from external API: {exc.response.text}")
        created_prompt = response.json()
        return PromptResponse(title=created_prompt["title"], description=created_prompt["description"])