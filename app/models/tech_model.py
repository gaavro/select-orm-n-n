from . import db
from . import db
from app.configs.database import db
from app.configs.database import db
from datetime import datetime, timedelta
from sqlalchemy.orm import backref, relationship
from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String




@dataclass
class Tech(db.Model):
    id:int
    name:str
    

    __tablename__='tech'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    
    


    
    # developers = relationship("Developer", backref=backref("developers"))