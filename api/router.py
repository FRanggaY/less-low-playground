from fastapi import APIRouter

from .endpoints import heroes

router = APIRouter()

router.include_router(heroes.router, prefix="/heroes", tags=["Heroes"])
