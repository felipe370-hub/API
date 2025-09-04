# Configurações da API
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    API_NAME = os.getenv("API_NAME", "Minha API FastAPI")
    API_VERSION = os.getenv("API_VERSION", "1.0.0")
    API_DESCRIPTION = os.getenv("API_DESCRIPTION", "API simples com endpoints /health e /me")

    ME_NOME = os.getenv("ME_NOME", "")
    ME_EMAIL = os.getenv("ME_EMAIL", "")
    ME_CURSO = os.getenv("ME_CURSO", "")
    ME_GITHUB = os.getenv("ME_GITHUB", "")
    ME_CIDADE = os.getenv("ME_CIDADE", "")
    ME_INTERESSES = os.getenv("ME_INTERESSES", "").split(",") if os.getenv("ME_INTERESSES") else []