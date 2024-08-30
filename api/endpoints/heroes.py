from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("")
async def read_heroes(
    is_active: bool = Query(...),
):
    """
        ## read heroes
    """

    status_code = status.HTTP_200_OK
    message = 'OK'
    datas = [
        {
            'id': 1,
            'title': 'BT-001',
        },
        {
            'id': 2,
            'title': 'Zero Hawk Knight',
        },
    ]

    response = {
        'status': status_code,
        'message': message,
        'data': datas,
        'meta': {
            'total': len(datas),
        }
    }

    return JSONResponse(content=response, status_code=status_code)
