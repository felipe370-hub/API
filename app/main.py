from fastapi import FastAPI
from app.core.config import Config
from app.routers import health

app = FastAPI(
    title=Config.API_NAME,
    version=Config.API_VERSION,
    description=Config.API_DESCRIPTION
)


@app.get("/")
def root():
    return {"status": "ok", "message": "API funcionando"}

app.include_router(health.router)
