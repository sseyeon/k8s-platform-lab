import socket

from fastapi import APIRouter

from app.config import APP_ENV, APP_NAME, APP_VERSION


router = APIRouter(
    prefix="/api",
    tags=["Application"],
)


@router.get("/info")
def application_info():
    return {
        "application": APP_NAME,
        "version": APP_VERSION,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
    }