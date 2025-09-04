from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.core.config import Config

router = APIRouter()

@router.get("/health")
def health():
    return JSONResponse(content={"status": "ok", "message": "API funcionando"})

@router.get("/me")
def me():
    return JSONResponse(content={
        "nome": Config.ME_NOME,
        "email": Config.ME_EMAIL,
        "curso": Config.ME_CURSO,
        "github": Config.ME_GITHUB,
        "cidade": Config.ME_CIDADE,
        "interesses": Config.ME_INTERESSES
    })
