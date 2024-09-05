from sqlalchemy import Column, String
from config.database import Base

class RukunWarga(Base):
    __tablename__ = 'rw'
    
    id_rw = Column(String, primary_key=True, index=True, unique=True)
    rw = Column(String, nullable=False)
