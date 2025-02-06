from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.apis.prompts import router as prompts_router

app = FastAPI()

# Configuração do CORS
origins = [
    "http://localhost:3000",  # Adicione o endereço do seu frontend aqui
    "http://127.0.0.1:3000",  # Adicione o endereço do seu frontend aqui
    "http://localhost:5173",  # Adicione o endereço do seu frontend aqui
    "http://127.0.0.1:5173",  # Adicione o endereço do seu frontend aqui
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prompts_router, prefix="/api")