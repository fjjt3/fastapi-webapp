from typing import Any
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative
import sqlalchemy

print(sqlalchemy.__version__)


@as_declarative()
class Base:
    id: Any
    __name__: str
    
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
        