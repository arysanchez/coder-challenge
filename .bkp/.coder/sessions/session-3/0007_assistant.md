### backend/main.py [coder:save]
```python
from fastapi import FastAPI
from app.apis.prompts import router as prompts_router

app = FastAPI()

app.include_router(prompts_router, prefix="/api")
```
[coder:end]