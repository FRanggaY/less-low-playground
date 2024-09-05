from sqlalchemy.orm import Session
from models.rw import RukunWarga

class RWRepository:
    def __init__(self, db: Session):
        self.db = db

    def read_rws(self):
        query = self.db.query(RukunWarga)
        return query.all()
    
    def read_rw(self, id_rw: str):
        query = self.db.query(RukunWarga).filter(RukunWarga.id_rw == id_rw)
        return query.first()  
    
    def read_rw_by_name(self, rw: str):
        query = self.db.query(RukunWarga).filter(RukunWarga.rw == rw)
        return query.first()  
    
    def count_rw(self):
        return self.db.query(RukunWarga).count()