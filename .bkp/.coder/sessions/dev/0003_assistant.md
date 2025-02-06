Vamos criar a infraestrutura de backend usando FastAPI e incluir as rotas para criar e listar prompts conforme solicitado.

### backend/main.py [coder:save]
```python
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from uuid import uuid4

app = FastAPI()

# Models
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

# Dependency to simulate authentication
def get_current_user(token: str = Depends()):
    if token != "valid-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return "user-id"

# Routes
@app.post("/v1/prompt-templates", response_model=Prompt)
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

@app.get("/v1/prompt-templates", response_model=List[PromptResponse])
async def list_prompts():
    return [PromptResponse(title=prompt.title, description=prompt.description) for prompt in prompts_db]
```
[coder:end]

### Explicação

1. **Modelos**: Definimos os modelos `PromptVariable`, `Prompt`, `CreatePromptRequest` e `PromptResponse` usando Pydantic. Esses modelos ajudam a validar e serializar os dados.

2. **Banco de Dados em Memória**: Utilizamos uma lista `prompts_db` para armazenar os prompts em memória. Em um ambiente de produção, você usaria um banco de dados real.

3. **Autenticação Simulada**: Criamos uma dependência `get_current_user` para simular a autenticação usando um token. Se o token não for válido, uma exceção HTTP 401 é levantada.

4. **Rotas**:
   - **POST /v1/prompt-templates**: Cria um novo prompt. A rota espera um corpo de requisição conforme o modelo `CreatePromptRequest` e retorna o prompt criado.
   - **GET /v1/prompt-templates**: Lista todos os prompts, retornando apenas o título e a descrição de cada prompt.

### Como usar

- **Criar Prompt**: Envie uma requisição POST para `/v1/prompt-templates` com o corpo da requisição no formato `CreatePromptRequest` e um cabeçalho de autorização com um token válido.
- **Listar Prompts**: Envie uma requisição GET para `/v1/prompt-templates` para obter uma lista de prompts com apenas o título e a descrição.

Essa infraestrutura de backend permitirá que você crie e liste prompts conforme necessário, integrando-se facilmente com o frontend que você já possui.