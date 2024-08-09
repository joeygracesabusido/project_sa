from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional
from datetime import datetime, date , timedelta
from fastapi.responses import JSONResponse

from pydantic import BaseModel

# from authentication.authenticate_user import get_current_user
from apps.views.company import CompanyNameComp

company_router = APIRouter(include_in_schema=False)

class Company(BaseModel):
    company_name: str 
    type_of_company: str
    address: str 
    contact_person: str 
    email_add: str 
    date_created: Optional[datetime] = None
   
    # date_created: Optional[datetime]

    class Config:
        from_attributes = True


@company_router.post("/api-insert-company/")
async def api_insert_cost_elements(items:Company):

    # if username == 'joeysabusido' or username == 'eliza' or username == 'drdc-admin':
    try:
    
        CompanyNameComp.insert_company_name(company_name=items.company_name,
                                            type_of_company=items.type_of_company,
                                            address=items.address,contact_person=items.contact_person,
                                            email_add=items.email_add)
        return {"message": "Data has been saved"}
    except Exception as e:
        error_message = str(e)
        raise HTTPException(status_code=500, detail=error_message)  

    # raise HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Not Authorized",
    #     # headers={"WWW-Authenticate": "Basic"},
    # )