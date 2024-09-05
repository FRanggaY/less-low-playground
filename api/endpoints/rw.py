from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session


from config.database import get_db
from services.rw_service import RWService

router = APIRouter()

@router.get("")
async def read_all_rw(
    db: Session = Depends(get_db),
    ):
    """
        ## Get all rws
    """

    rw_service = RWService(db)
    rws = []
    total_items = 0

    rws = rw_service.rw_repository.read_rws()
    total_items = rw_service.rw_repository.count_rw()

    if not rws:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No rw found")

    status_code = status.HTTP_200_OK
    message = ''
    datas = []
    for rw in rws:
        datas.append({
            'id_rw': rw.id_rw,
            'rw': rw.rw,
        })
        
    response = {
        'status': status_code,
        'message': message,
        'data': datas,
        'total_items': total_items 
    }

    return JSONResponse(content=response, status_code=status_code)