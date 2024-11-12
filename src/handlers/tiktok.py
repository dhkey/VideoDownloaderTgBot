from aiogram import Router, F
from aiogram.types import Message

from api.tiktok import TikTokDownloader

router = Router()

@router.message(F.text)
async def tiktokHandler(message: Message):
    if "tiktok" in message.text:    
    