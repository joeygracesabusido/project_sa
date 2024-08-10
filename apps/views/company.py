from sqlmodel import Field, Session,  create_engine,select,func,funcfilter,within_group,Relationship,Index

from apps.models.company import CompanyName
from databases.database import connectionDB
from typing import Optional
from datetime import date, datetime




engine = connectionDB.conn()


class CompanyNameComp(): # this class is for payroll  Transaction

    @staticmethod
    def insert_company_name(company_name,type_of_company,
                            address,contact_person,email_add): # this is for inserting balance sheet 
        
        insertData = CompanyName(company_name=company_name,type_of_company=type_of_company,
                                 address=address,contact_person=contact_person,
                                 email_add=email_add)
        

        session = Session(engine)

        session.add(insertData)
        
        session.commit()

        session.close()

    @staticmethod
    def get_company(): # this function is to get a list of Company
        with Session(engine) as session:
            try:
                statement = select(CompanyName).order_by(CompanyName.company_name)

               
                            
                results = session.exec(statement) 

                data = results.all()
                
                return data
            except :
                return None

    