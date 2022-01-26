import sqlite3
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import adminlar
from keyboards.default.asosiy_bolim import *
from loader import dp, bot,d

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.first_name
    try:
        d.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        pass

    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=ingliz)
    user = message.from_user.username
    await bot.send_message(chat_id=adminlar,text=f'Botga yangi foydalanuvchi @{user} qoshildi')
