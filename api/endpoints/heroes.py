from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse

from services.hero_service import HeroService

router = APIRouter()

@router.get("")
async def read_heroes(
    name: str = Query(...),
):
    """
        ## read heroes
    """

    hero_service = HeroService(name)

    status_code = status.HTTP_200_OK
    message = 'OK'
    datas = hero_service.hero_repository.get_static_data()

    response = {
        'status': status_code,
        'message': message,
        'data': datas,
        'meta': {
            'total': len(datas),
        }
    }

    return JSONResponse(content=response, status_code=status_code)
