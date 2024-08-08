from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from models.company import CompanyName
from databases.database import connectionDB
from typing import Optional
from datetime import date, datetime




engine = connectionDB.conn()


class CompanyNameComp(): # this class is for payroll  Transaction

    @staticmethod
    def insert_company_name(company_name): # this is for inserting balance sheet 
        
        insertData = CompanyName(company_name=company_name)
        

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()

    