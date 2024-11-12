from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from api.downloader import download
from threading import Thread
import os 
from aiogram.types import InputFile, FSInputFile
import re 

router = Router()


@router.message()
async def tiktokHandler(message: Message, state: FSMContext):

    
    await message.answer("downloading")
    
    downloading_thread = Thread(target=download,args=(message.text, message.chat.id))
    downloading_thread.start()
    downloading_thread.join()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    downloads_path = os.path.join(script_dir, "..", "downloads")
    downloads_path = os.path.normpath(downloads_path)
    
    file_path = f"{downloads_path}/{message.from_user.id}.mp4"
    
    video = FSInputFile(file_path, filename=os.path.basename(file_path))
    
    await message.bot.send_video(
        chat_id = message.chat.id,
        video = video
    )

    os.remove(file_path)