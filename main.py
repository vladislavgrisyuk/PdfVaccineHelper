from typing import Any
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types.message_entity import MessageEntity
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from talent import talentS
import helper

storage = MemoryStorage()

token = '5014356260:AAExs4--9I4IcNkawOxwrf6fM3xFaidGRiU'


bot = Bot(token)
dp = Dispatcher(bot, storage=storage)


class TalentState(StatesGroup):
    base = State()
    choose = State()
    Chosen = State()


@dp.message_handler(commands=['reset'])
async def begin(message: types.Message, state: FSMContext):
    await bot.send_message(message.chat.id, '<i>Возвар в главное меню</i>', parse_mode='HTML')



@dp.message_handler(commands=['start'])
async def begin(message: types.Message):
    await bot.send_message(message.chat.id, '<i>asd</i>', parse_mode='HTML')
    #await bot.send_document(message.chat.id, document=open('main.py', 'rb'))




async def on_startup(dispatcher):
    commands = [
        {
            "command": "start",
            "description": "Start using bot"
        },
        {
            "command": "help",
            "description": "Display help"
        },
        {
            "command": "calc",
            "description": "Посчитать силу умельца"
        }
    ]
    await bot.set_my_commands(commands)


executor.start_polling(dp, on_startup=on_startup, skip_updates=True)

# if __name__ == '__main__':
#     main()