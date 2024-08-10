from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel

# from authentication.authenticate_user import get_current_user
from apps.views.company import CompanyNameComp

company_router = APIRouter(include_in_schema=True)

class Company(BaseModel):
    company_name: str 
    type_of_company: str
    address: str 
    contact_person: str 
    email_add: str 
    # date_created: Optional[datetime] = None
   
    # date_created: Optional[datetime]

    class Config:
        from_attributes = True


@company_router.post("/api-insert-company/")
async def api_insert_company(items:Company):

    # if username == 'joeysabusido' or username == 'eliza' or username == 'drdc-admin':
    try:
    
        
        CompanyNameComp.insert_company_name(**items.dict())

        return {"message": "Data has been saved"}
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)  

    # raise HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Not Authorized",
    #     # headers={"WWW-Authenticate": "Basic"},
    # )

@company_router.get("/api-get-company/")
async def api_get_company() -> List:

    
    try:
        results = CompanyNameComp.get_company()

        company_list = [{
            "id": i.id,
            "company_name": i.company_name,
            "type_of_company": i.type_of_company,
            "address": i.address,
            "contact_person": i.contact_person,
            "email_add": i.email_add
        }
         for i in results
        ]


        
        return company_list
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)  

   