from fastapi import (
    APIRouter,
    Request,
    Response,
    status,
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from starlette.status import HTTP_415_UNSUPPORTED_MEDIA_TYPE, HTTP_201_CREATED

router = APIRouter(
    prefix='',
    tags=['root'],
)

#
# @router.get(
#     '/',
#     response_model=None,
#     status_code=status.HTTP_202_ACCEPTED,
# )
# async def root(request: Request):
#
#     return Response('Bot is proceeding normally', status_code=status.HTTP_202_ACCEPTED)

templates = Jinja2Templates(directory="templates")
router.mount("/static", StaticFiles(directory="static"), name="static")


@router.get(
    "/",
    response_model=None,
    status_code=status.HTTP_202_ACCEPTED,
)
async def root(request: Request):
    data = {
        "page": "Home page"
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": data})
