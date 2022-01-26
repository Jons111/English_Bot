
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,CallbackQuery

from data.config import botlar,adminlar
from keyboards.inline.post import confirmation_keyboard,post_callback
from loader import dp,bot
from states.holatlar import Postlar


@dp.message_handler(text='Reklama')
async def create_post(message: Message):
    await message.answer('Chop etish uchun post yuboring')
    await Postlar.chop_etish.set()
@dp.message_handler(state=Postlar.chop_etish)
async def enter_message(message:Message,state:FSMContext):
    await state.update_data(text=message.html_text,username=f'@{message.from_user.first_name}')
    await message.answer(f'Postni tekshirish uchun yuboraymi?',
                         reply_markup=confirmation_keyboard)
    await Postlar.rad_etish.set()
@dp.callback_query_handler(post_callback.filter(action='post'), state=Postlar.rad_etish)
async def confirm_post(call:CallbackQuery,state:FSMContext):
    async with state.proxy() as data:
        text = data.get('text')
        username = data.get('username')
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Post adminga yuborildi')
    await bot.send_message(adminlar, f"Foydalanuvchi {username} quyidagi postni chop etmoqchi:")
    await bot.send_message(adminlar,text,parse_mode='HTML',reply_markup=confirmation_keyboard)
@dp.callback_query_handler(post_callback.filter(action='cancel'),state=Postlar.rad_etish)
async  def cancel_post(call:CallbackQuery,state:FSMContext):
    await state.finish()
    await call.message.edit_reply_markup()
    await call.message.answer('Post rad etildi')
@dp.message_handler(state=Postlar.rad_etish)
async def post_unkown(message:Message):
    await message.answer("Chop etish yoki rad etishni tanlang")


@dp.callback_query_handler(post_callback.filter(action='post'),user_id=adminlar)
async def approve_post(call : CallbackQuery):
    await call.answer('Chop etishga ruhsat berdingiz.',show_alert=True)
    target_chanel = botlar
    message = await call.message.edit_reply_markup()
    await bot.send_message(chat_id=target_chanel,text=f'{message}')
@dp.callback_query_handler(post_callback.filter(action='cancel'),user_id=adminlar)
async def decline_post(call:CallbackQuery):
    await call.answer('Post rad etildi.',show_alert=True)
    await call.message.edit_reply_markup()
