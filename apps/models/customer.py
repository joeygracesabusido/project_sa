from sqlmodel import Field, Session, SQLModel, create_engine,select,func,funcfilter,within_group,Relationship,Index
from typing import Optional
from decimal import Decimal


import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, '..')
sys.path.append(parent_dir)


from databases.database import connectionDB
from datetime import date, datetime, timezone

engine = connectionDB.conn()


class CustomerName(SQLModel, table=True):
    """This function is for Company Name"""
    __tablename__ = 'companyName'
    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(index=True, unique=True)
    type_of_company: str = Field(default=None)
    address: str = Field(default=None)
    contact_person: str = Field(default=None)
    email_add: str = Field(default=None)
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    __table_args__ = (Index("idx_companyName_unique", "company_name", unique=True),)

def create_db_and_tables():
    
    SQLModel.metadata.create_all(engine)

# create_db_and_tables()

