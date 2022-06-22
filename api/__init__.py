from fastapi import APIRouter

from api import bot, bot_proactive, root

router = APIRouter()
router.include_router(bot.router)
router.include_router(bot_proactive.router)
router.include_router(root.router)



