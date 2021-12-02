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
class Developer(db.Model):
    id:int
    name:str
    age:int
    job_role:str
    
    __tablename__='developer'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    job_role = Column(String, nullable=False)
    

    result = relationship('Tech', secondary='developer_tech', backref='developer')
    
    # technologies = relationship("Tech", backref=backref("tech"))

    