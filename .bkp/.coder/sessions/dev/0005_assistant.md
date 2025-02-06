Não, não precisamos manter as funções no arquivo `backend/main.py` agora que elas foram movidas para `prompts.py`. O arquivo `main.py` deve apenas inicializar o FastAPI e incluir o roteador de APIs.

Aqui está o conteúdo atualizado do arquivo `backend/main.py`:

### backend/app/main.py [coder:save]
```python
from fastapi import FastAPI
from .apis import router as api_router

app = FastAPI()

app.include_router(api_router)
```
[coder:end]