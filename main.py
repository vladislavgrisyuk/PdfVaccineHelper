from typing import Any
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message_entity import MessageEntity
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from talent import talentS
import pdfhelper
import helper
from replacements import getReplacementsV
from random import randint
import os
from dotenv import load_dotenv

load_dotenv()

storage = MemoryStorage()

token = os.getenv('TOKEN')


bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


class TalentState(StatesGroup):
    base = State()
    choose = State()
    Chosen = State()


@dp.message_handler(commands=['vlad'])
async def begin(message: types.Message, state: FSMContext):
    pdfhelper.go('v.pdf', getReplacementsV())
    await bot.send_document(message.chat.id, document=open('v.result.pdf', 'rb'))



@dp.message_handler(commands=['nastya'])
async def begin(message: types.Message):
    r = getReplacementsV()
    pdfhelper.go('n.pdf', r)
    await bot.send_document(message.chat.id, document=open('n.result.pdf', 'rb'))
    
@dp.message_handler(commands=['all'])
async def begin(message: types.Message):
    rSmall = randint(1, 5)
    rTimeHours = randint(9,11)
    rTimeMinutes = randint(0,40)
    time = str(rTimeHours).zfill(2) + ':' + str(rTimeMinutes).zfill(2)
    timeMinutesPlus = rTimeMinutes + 15
    timePlus = str(rTimeHours).zfill(2) + ':' + str(timeMinutesPlus).zfill(2)
    
    r = getReplacementsV(rTimeHours, rTimeMinutes)
    pdfhelper.go('n.pdf', r)
    await bot.send_document(message.chat.id, document=open('n.result.pdf', 'rb'))
    
    r = getReplacementsV(rTimeHours, rTimeMinutes + rSmall)
    pdfhelper.go('v.pdf', r)
    await bot.send_document(message.chat.id, document=open('v.result.pdf', 'rb'))


async def on_startup(dispatcher):
    commands = [
        {
            "command": "/nastya",
            "description": "Certificate for nastya"
        },
        {
            "command": "/vlad",
            "description": "Certificate for vlad"
        },
        {
            "command": "/all",
            "description": "Both certificates"
        }
    ]
    await bot.set_my_commands(commands)


executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

# if __name__ == '__main__':
#     main()