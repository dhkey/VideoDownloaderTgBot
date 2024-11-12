from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from api.downloader import download
from threading import Thread
import os 
from aiogram.types import InputFile, FSInputFile

router = Router()

def checkUrl(url): #FIXME make normal
    for platform in ["tiktok", "reel", "facebook"]: #TODO add youtube
        if platform in url and "https" in url:
            return True
    return False

@router.message()
async def urls_handler(message: Message, state: FSMContext):
    
    if not checkUrl(message.text):
        return 
    
    await message.answer("downloading...")
    
    downloading_thread = Thread(target=download,args=(message.text, message.chat.id))
    downloading_thread.start()
    downloading_thread.join()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    downloads_path = os.path.join(script_dir, "..", "downloads")
    downloads_path = os.path.normpath(downloads_path)
    
    file_path = f"{downloads_path}/{message.chat.id}.mp4"
    
    video = FSInputFile(file_path, filename=os.path.basename(file_path))
    
    bot_info = await message.bot.get_me()
    username = bot_info.username
    
    await message.bot.send_video(
        chat_id = message.chat.id,
        video = video,
        caption = f"downloaded by @{ username }"
    )

    os.remove(file_path)