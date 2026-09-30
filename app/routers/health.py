from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/live")
def liveness():
    return {
        "status": "UP",
    }


@router.get("/ready")
def readiness():
    return {
        "status": "READY",
    }