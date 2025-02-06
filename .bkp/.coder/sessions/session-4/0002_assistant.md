Para resolver o problema de CORS entre o FastAPI (backend) e o seu frontend, você pode configurar o middleware de CORS no FastAPI. Vou adicionar essa configuração no arquivo `backend/main.py`.

### backend/main.py [coder:save]
```
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apis.prompts import router as prompts_router

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:3000",  # Adicione o endereço do seu frontend aqui
    "http://127.0.0.1:3000",  # Adicione o endereço do seu frontend aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prompts_router, prefix="/api")
```
[coder:end]

Com essa configuração, o FastAPI permitirá requisições do seu frontend que está rodando em `http://localhost:3000` ou `http://127.0.0.1:3000`. Se o seu frontend estiver em outro endereço, basta adicionar esse endereço na lista `origins`.