from fastapi import FastAPI

from app.routers import health, info

app = FastAPI(
    title="Kubernetes Platform Lab",
    description="Sample FastAPI application for Kubernetes platform lab",
    version="1.0.0",
)

app.include_router(health.router)
app.include_router(info.router)


@app.get("/")
def root():
    return {
        "message": "Kubernetes Platform Lab",
        "status": "running",
    }