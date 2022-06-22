import api
import uvicorn

from config.conf import FAST_API_CONF, TAGS_META
from db.engine import DATABASE, METADATA, ENGINE
from setup.logger import CustomLogger
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


logger = CustomLogger.get_logger('bot')


app = FastAPI(
    title='FastApi Microsoft Bot Framework & Durger',
    description='Microsoft Bot Implementation & Durger',
    version='1.0.0',
    openapi_tags=TAGS_META,
)

app.include_router(api.router)

METADATA.create_all(ENGINE)
app.state.database = DATABASE


@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        logger.info('Connection to database has been established')


@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()
        logger.info('Connection to database has been closed')




if __name__ == '__main__':
    uvicorn.run('app:app', host=FAST_API_CONF.HOST, port=FAST_API_CONF.PORT, log_level='debug', reload=True)
