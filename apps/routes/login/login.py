from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional


from datetime import datetime, timedelta

# from ..authentication.utils import OAuth2PasswordBearerWithCookie



login_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")




@login_router.get("/", response_class=HTMLResponse)
async def api_login(request: Request):
    return templates.TemplateResponse("login/login.html", {"request":request}) 



    