from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy import DateTime, String, Column
from sqlalchemy.sql import func
from uuid import uuid4

DeclarativeBase: DeclarativeMeta = declarative_base()

class BaseModel(DeclarativeBase):
    __abstract__ = True
    id = Column(String, default=lambda: str(uuid4()), primary_key=True)
    date_created = Column(DateTime, default=func.now())
    date_updated = Column(DateTime, default=func.now(), onupdate=func.now())
