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
class DeveloperTech(db.Model):
    developer_id:int
    tech_id:str
    

    __tablename__='developer_tech'

    developer_id = Column(Integer, ForeignKey("developer.id"), primary_key=True)
    tech_id = Column(Integer, ForeignKey("tech.id"), primary_key=True)
    
    


    