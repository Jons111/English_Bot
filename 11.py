from typing import Union
from aiogram import Bot

async def tekshirish(user_id,kanal:Union[str,int]):
    bot = Bot.get_current()
    azo = await bot.get_chat_member(user_id=user_id,chat_id=kanal)
    return azo.is_chat_member()
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
guruh=['@aloqa_operatorlar_bot','@Frondend_boshlovchilar']
azo_bolish=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕ Azo bolish ➕',url='https://t.me/Frondend_boshlovchilar'),
            InlineKeyboardButton(text='➕ Azo bolish ➕',url='@aloqa_operatorlar_bot')
        ]
    ]
)



class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn =  'Quyidagi kanalga azo boling va qayta startni bosing\n'

        dastlabki_holati = True
        for k in guruh:
            holat = await tekshirish(user_id=user_id,kanal=k)
            dastlabki_holati*=holat
            kanal = await bot.get_chat(k)
            if not holat:
             link = await kanal.export_invite_link()

        if not dastlabki_holati:
            await xabar.message.answer(matn,disable_web_page_preview=True,reply_markup=azo_bolish)
            raise CancelHandler()

import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '5045737412:AAFIl8KMjzCAJUccQZQEtfBXnZ7pah6wvLs'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("📙1-sinf kitoblari📚"),
        KeyboardButton("📙2-sinf kitoblari📚"),
        KeyboardButton("📙3-sinf kitoblari📚"),
        KeyboardButton("📙4-sinf kitoblari📚"),
        KeyboardButton("📙5-sinf kitoblari📚"),
        KeyboardButton("📙6-sinf kitoblari📚"),
        KeyboardButton("📙7-sinf kitoblari📚"),
        KeyboardButton("📙8-sinf kitoblari📚"),
        KeyboardButton("📙9-sinf kitoblari📚"),
        KeyboardButton("📙10-sinf kitoblari📚"),
        KeyboardButton("📙11-sinf kitoblari📚")
        )

    await message.reply("Salom!\nBu botda 1-sinfdan 11- sinfgacha maktab darsliklari bor!\nNechinchi sinf kitob kerak."
                                , reply_markup=keyboard)

    @dp.message_handler(text='📙1-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/122'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await g.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙2-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/12'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/13'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/14'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/15'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/16'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/17'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/18'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/19'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/20'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/21'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙3-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/22'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/23'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/24'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/25'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/26'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/27'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/28'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/29'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/30'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/31'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙4-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/32'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/33'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/34'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/35'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/36'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/37'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/38'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/39'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/40'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/41'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙5-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/42'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/43'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/44'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/45'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/46'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/47'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/48'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/49'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/50'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/51'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙6-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/52'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/53'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/54'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/55'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/56'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/57'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/58'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/59'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/60'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/61'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙7-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/62'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/63'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/64'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/65'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/66'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/67'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/68'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/69'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/70'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/71'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙8-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/72'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/73'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/74'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/75'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/76'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/77'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/78'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/79'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/80'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/81'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙9-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/82'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/83'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/84'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/85'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/86'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/87'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/88'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/89'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/90'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/91'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙10-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/92'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/93'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/94'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/95'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/96'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/97'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/98'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/99'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/100'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/101'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")

    @dp.message_handler(text='📙11-sinf kitoblari📚')
    async def test(msg: types.Message):
        link1 = 'https://t.me/ddddddddddddd35858i4jfncj/102'
        link2 = 'https://t.me/ddddddddddddd35858i4jfncj/103'
        link3 = 'https://t.me/ddddddddddddd35858i4jfncj/104'
        link4 = 'https://t.me/ddddddddddddd35858i4jfncj/105'
        link5 = 'https://t.me/ddddddddddddd35858i4jfncj/106'
        link6 = 'https://t.me/ddddddddddddd35858i4jfncj/107'
        link7 = 'https://t.me/ddddddddddddd35858i4jfncj/108'
        link8 = 'https://t.me/ddddddddddddd35858i4jfncj/109'
        link9 = 'https://t.me/ddddddddddddd35858i4jfncj/110'
        link10 = 'https://t.me/ddddddddddddd35858i4jfncj/111'
        await msg.reply_document(document=link1, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link2, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link3, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link4, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link5, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link6, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link7, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link8, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link9, caption="@Sindorov_Bekhzod")
        await msg.reply_document(document=link10, caption="@Sindorov_Bekhzod")




@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


executor.start_polling(dp, skip_updates=True)