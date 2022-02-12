from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

b_vlad = KeyboardButton('Влад тест')
b_nastya = KeyboardButton('Настя тест')
b_all = KeyboardButton('Оба теста')

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).row(
    b_all).row(b_vlad, b_nastya)
