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

from models.company import CompanyName

engine = connectionDB.conn()


class User(SQLModel, table=True):
    """This is to create user Table"""
    __tablename__ = 'user'
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=70)
    last_name: str = Field(max_length=70)
    username: str = Field(index=True, unique=True)
    hashed_password: str = Field(nullable=False)
    email_add: str = Field(nullable=False)
    role: str = Field(max_length=70, default=None)
    amount: Decimal = Field(default=0, max_digits=20, decimal_places=2)
    is_active: bool = Field(default=False)
    company_name: Optional[int] = Field(default=None, foreign_key="CompanyName.id")
    date_updated: Optional[datetime] = Field(default=None)
    date_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    __table_args__ = (Index("idx_user_unique", "username", unique=True),)
    __table_args__ = (Index("idx_email_add_unique", "email_add", unique=True),)

def create_db_and_tables():
    
    SQLModel.metadata.create_all(engine)

create_db_and_tables()

