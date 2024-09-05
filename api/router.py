from fastapi import APIRouter

from .endpoints import heroes, rw

router = APIRouter()

router.include_router(heroes.router, prefix="/heroes", tags=["Heroes"])
router.include_router(rw.router, prefix="/rw", tags=["Rukun Warga"])
