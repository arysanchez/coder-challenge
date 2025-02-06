Vamos criar a estrutura de pastas para o backend e organizar as rotas dentro da pasta `backend/app/apis`.

### Estrutura de Pastas

```
backend/
├── app/
│   ├── apis/
│   │   ├── __init__.py
│   │   ├── prompts.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── prompt.py
│   ├── main.py
```

### backend/app/apis/__init__.py [coder:save]
```python
from fastapi import APIRouter
from .prompts import router as prompts_router

router = APIRouter()
router.include_router(prompts_router, prefix="/v1/prompt-templates", tags=["prompts"])
```
[coder:end]

### backend/app/apis/prompts.py [coder:save]
```python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from datetime import datetime
from uuid import uuid4
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
```
[coder:end]

### backend/app/core/__init__.py [coder:save]
```python
# This file can be left empty or used for initialization code for the core module
```
[coder:end]

### backend/app/core/config.py [coder:save]
```python
# Configuration settings can be added here
```
[coder:end]

### backend/app/models/__init__.py [coder:save]
```python
# This file can be left empty or used for initialization code for the models module
```
[coder:end]

### backend/app/models/prompt.py [coder:save]
```python
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
    title: str
    description: str

# In-memory storage for prompts
prompts_db = []
```
[coder:end]

### backend/app/main.py [coder:save]
```python
from fastapi import FastAPI
from .apis import router as api_router

app = FastAPI()

app.include_router(api_router)
```
[coder:end]

### Explicação

1. **Estrutura de Pastas**: Organizamos o código em diferentes pastas para melhor modularidade e manutenção:
   - `apis`: Contém os arquivos de rotas.
   - `core`: Pode conter configurações e inicializações.
   - `models`: Contém os modelos de dados.

2. **Rotas**: As rotas para criar e listar prompts estão definidas no arquivo `prompts.py` dentro da pasta `apis`.

3. **Modelos**: Os modelos de dados estão definidos no arquivo `prompt.py` dentro da pasta `models`.

4. **Arquivo Principal**: O arquivo `main.py` inicializa o FastAPI e inclui o roteador de APIs.

Essa estrutura modular facilita a manutenção e a escalabilidade do projeto.