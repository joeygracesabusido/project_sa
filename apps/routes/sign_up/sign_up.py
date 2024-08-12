from fastapi import APIRouter, Body, HTTPException, Depends, Request, Response, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from typing import Union, List, Optional


from datetime import datetime, timedelta

# from ..authentication.utils import OAuth2PasswordBearerWithCookie



temp_login_router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="apps/templates")




@temp_login_router.get("/-temp-sign-up/", response_class=HTMLResponse)
async def api_login(request: Request):
    return templates.TemplateResponse("sign_up/signUp.html", {"request":request}) 



