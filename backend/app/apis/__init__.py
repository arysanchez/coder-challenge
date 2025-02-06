from fastapi import APIRouter
from .prompts import router as prompts_router

router = APIRouter()
router.include_router(prompts_router, prefix="/v1/prompt-templates", tags=["prompts"])