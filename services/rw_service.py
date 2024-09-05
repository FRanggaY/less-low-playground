from sqlalchemy.orm import Session
from repositories.rw_repository import RWRepository

class RWService:
    def __init__(self, db: Session):
        self.db = db
        self.rw_repository = RWRepository(db)
        
    
