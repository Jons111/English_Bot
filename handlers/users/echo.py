from aiogram import types
from data.config import adminlar
from loader import dp,d,bot


# Echo bot
@dp.message_handler(commands='baza')
async def bot_echo(message: types.Message):
    d.create_table_users()
    await message.answer(text='Baza yaratildi')

@dp.message_handler(state=None)
async def bot_start(message: types.Message):
    user = message.from_user.username
    await message.answer(text=f'@{user} habaringiz adminga yuborildi')
    await bot.send_message(chat_id=adminlar,text=f'Foydalanuvchi @{user} sizga {message.text} xabarni yubordi')