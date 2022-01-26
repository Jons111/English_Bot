from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.asosiy_bolim import *
from data.config import adminlar
from loader import dp,bot
from states.send_message import Vaziyatlar


@dp.message_handler(text="To be fe'llari")
async def bot_start(message: types.Message):
    await message.answer(text='Please choice',reply_markup=tobe_button)
@dp.message_handler(text="Tag questions")
async def bot_start(message: types.Message):
    link = 'https://t.me/dddddddddddddddddddd122/227'
    await message.reply_video(video=link,caption='@Makhmudov13_04')
@dp.message_handler(text='Am,is,are')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/2'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Was,were')
async def bot_start(message: types.Message):
    link2 = 'https://t.me/dddddddddddddddddddd122/3'
    await message.reply_video(video=link2,caption='@Makhmudov13_04')
@dp.message_handler(text='Will,Shall')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/4'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='🔙 Go back')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/2'
    await message.answer(text='You are come back',reply_markup=zamonlar_button)
@dp.message_handler(text='Zamonlar')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/4'
    await message.answer(text='Tenses',reply_markup=zamonlar_button)
@dp.message_handler(text='Past tenses')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/5'
    await message.answer(text='Choice',reply_markup=past_button)
@dp.message_handler(text='Past simple')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/5'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Past perfect')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/6'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Past perfect')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/6'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Past continuous')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/8'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Present tenses')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/6'
    await message.answer(text='Choice',reply_markup=present_button)
@dp.message_handler(text='Present simple')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/9'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Present continuous')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/10'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Present Perfect')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/11'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')

@dp.message_handler(text='🏠 Main menu')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/11'
    await message.answer(text='🏠 Main menu',reply_markup=ingliz)
@dp.message_handler(text='Future tenses')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/11'
    await message.answer(text='Future tenses',reply_markup=futere_button)
@dp.message_handler(text='Future simple')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/12'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Future continious')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/13'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Future Perfect')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/14'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text="Modal fe'llar")
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/11'
    await message.answer(text="Modal fe'llar",reply_markup=modal_fel_button)
@dp.message_handler(text='Can')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/15'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='May might')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/16'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Should')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/17'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='(be) able to')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/18'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Must')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/19'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Have to')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/22'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Need')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/21'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text="Qo'shma gaplar")
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/23'
    await message.answer(text='Choice',reply_markup=qoshma_gap_button)
@dp.message_handler(text='Ifli gaplar')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/23'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Wishli gaplar')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/24'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Passive voice')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/22'
    await message.answer(text='Choice',reply_markup=passive_button)
@dp.message_handler(text='Passive')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/25'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='If it said that....,He is said that')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/26'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='He is said that....')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/27'
    await message.reply_video(video=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='Reported speech')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/27'
    await message.answer(text='Choice',reply_markup=reported_button)
@dp.message_handler(text='🧑‍💻 Bot admini')
async def bot_start(message: types.Message):

    await message.answer(text='Bot 20.01.2022 da yaratildi\n ADMIN TG:@Makhmudov13_04\nTELEFON:+998905859461\nINSTAGRAM:bobur_9461')
@dp.message_handler(text='Ortga')
async def bot_start(message: types.Message):
    user = message.from_user.first_name
    await message.answer(text='Choice',reply_markup=ingliz)
@dp.message_handler(text='✍️ Fikr bildirish')
async def bot_start(message: types.Message):
    await message.answer(text='Qanday fikringiz bolsa botda yozib qoldirishingiz mumkin biz albatta fikringizni inobatga olamiz')
    await Vaziyatlar.qabul_qilish.set()
@dp.message_handler(state=Vaziyatlar.qabul_qilish)
async def bot_start(message: types.Message,state:FSMContext):
    get_message = message.text
    user = message.from_user.username
    await bot.send_message(chat_id=adminlar,text=f'Foydalanuvchi @{user} botga {get_message} fikr yubordi')
    await message.answer(text='Fikir adminga yuborildi fikringiz uchun rahmat')
    await state.finish()
@dp.message_handler(text='🔴 Red Raymond Morphy lessons')
async def bot_start(message: types.Message):
    await message.answer(text='Choice',reply_markup=qizil_morfy_button)
@dp.message_handler(text='🔴 1-5 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/28'
    link2 = 'https://t.me/dddddddddddddddddddd122/29'
    link3 = 'https://t.me/dddddddddddddddddddd122/30'
    link4 = 'https://t.me/dddddddddddddddddddd122/31'
    link5 = 'https://t.me/dddddddddddddddddddd122/32'
    await message.reply_video(video=link1, caption='Unit 1\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 2\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 3\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 4\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 5\n@Makhmudov13_04')
@dp.message_handler(text='🔴 5-10lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/33'
    link2 = 'https://t.me/dddddddddddddddddddd122/34'
    link3 = 'https://t.me/dddddddddddddddddddd122/35'
    link4 = 'https://t.me/dddddddddddddddddddd122/36'
    link5 = 'https://t.me/dddddddddddddddddddd122/37'
    await message.reply_video(video=link1,caption='Unit 6\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 7\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 8\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 9\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 10\n@Makhmudov13_04')
@dp.message_handler(text='🔴 10-15 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/38'
    link2 = 'https://t.me/dddddddddddddddddddd122/39'
    link3 = 'https://t.me/dddddddddddddddddddd122/40'
    link4 = 'https://t.me/dddddddddddddddddddd122/42'
    link5 = 'https://t.me/dddddddddddddddddddd122/43'
    await message.reply_video(video=link1,caption='Unit 11\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 12\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 13\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 14\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 15\n@Makhmudov13_04')
@dp.message_handler(text='🔴 15-20 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/44'
    link2 = 'https://t.me/dddddddddddddddddddd122/45'
    link3 = 'https://t.me/dddddddddddddddddddd122/46'
    link4 = 'https://t.me/dddddddddddddddddddd122/47'
    link5 = 'https://t.me/dddddddddddddddddddd122/48'
    await message.reply_video(video=link1,caption='Unit 16\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 17\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 18\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 19\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 20\n@Makhmudov13_04')
@dp.message_handler(text='🔴 20-30 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/49'
    link2 = 'https://t.me/dddddddddddddddddddd122/50'
    link3 = 'https://t.me/dddddddddddddddddddd122/51'
    link4 = 'https://t.me/dddddddddddddddddddd122/52'
    link5 = 'https://t.me/dddddddddddddddddddd122/53'
    link6 = 'https://t.me/dddddddddddddddddddd122/54'
    link7 = 'https://t.me/dddddddddddddddddddd122/55'
    link8 = 'https://t.me/dddddddddddddddddddd122/57'
    link9 = 'https://t.me/dddddddddddddddddddd122/58'
    link10 = 'https://t.me/dddddddddddddddddddd122/59'
    await message.reply_video(video=link1, caption='Unit 21\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 22\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 23\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 24\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 25\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 26\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 27\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 28\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 29\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 30\n@Makhmudov13_04')
@dp.message_handler(text='🔴 30-40 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/60'
    link2 = 'https://t.me/dddddddddddddddddddd122/61'
    link3 = 'https://t.me/dddddddddddddddddddd122/62'
    link4 = 'https://t.me/dddddddddddddddddddd122/63'
    link5 = 'https://t.me/dddddddddddddddddddd122/64'
    link6 = 'https://t.me/dddddddddddddddddddd122/65'
    link7 = 'https://t.me/dddddddddddddddddddd122/66'
    link8 = 'https://t.me/dddddddddddddddddddd122/67'
    link9 = 'https://t.me/dddddddddddddddddddd122/68'
    link10 = 'https://t.me/dddddddddddddddddddd122/69'
    await message.reply_video(video=link1, caption='Unit 31\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 32\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 33\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 34\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 35\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 36\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 37\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 38\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 39\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 40\n@Makhmudov13_04')
@dp.message_handler(text='🔴 40-50 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/70'
    link2 = 'https://t.me/dddddddddddddddddddd122/71'
    link3 = 'https://t.me/dddddddddddddddddddd122/72'
    link4 = 'https://t.me/dddddddddddddddddddd122/73'
    link5 = 'https://t.me/dddddddddddddddddddd122/74'
    link6 = 'https://t.me/dddddddddddddddddddd122/75'
    link7 = 'https://t.me/dddddddddddddddddddd122/76'
    link8 = 'https://t.me/dddddddddddddddddddd122/77'
    link9 = 'https://t.me/dddddddddddddddddddd122/78'
    link10 = 'https://t.me/dddddddddddddddddddd122/79'
    await message.reply_video(video=link1, caption='Unit 41\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 42\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 43\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 44\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 45\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 46\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 47\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 48\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 49\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 50\n@Makhmudov13_04')
@dp.message_handler(text='🔴 50-70 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/80'
    link2 = 'https://t.me/dddddddddddddddddddd122/81'
    link3 = 'https://t.me/dddddddddddddddddddd122/82'
    link4 = 'https://t.me/dddddddddddddddddddd122/83'
    link5 = 'https://t.me/dddddddddddddddddddd122/84'
    link6 = 'https://t.me/dddddddddddddddddddd122/85'
    link7 = 'https://t.me/dddddddddddddddddddd122/86'
    link8 = 'https://t.me/dddddddddddddddddddd122/87'
    link9 = 'https://t.me/dddddddddddddddddddd122/88'
    link10 = 'https://t.me/dddddddddddddddddddd122/89'
    link11 = 'https://t.me/dddddddddddddddddddd122/90'
    link12 = 'https://t.me/dddddddddddddddddddd122/91'
    link13 = 'https://t.me/dddddddddddddddddddd122/92'
    link14 = 'https://t.me/dddddddddddddddddddd122/93'
    link15 = 'https://t.me/dddddddddddddddddddd122/94'
    link16 = 'https://t.me/dddddddddddddddddddd122/95'
    link17 = 'https://t.me/dddddddddddddddddddd122/96'
    link18 = 'https://t.me/dddddddddddddddddddd122/97'
    link19 = 'https://t.me/dddddddddddddddddddd122/98'
    link20 = 'https://t.me/dddddddddddddddddddd122/99'
    await message.reply_video(video=link1, caption='Unit 51\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 52\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 53\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 54\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 55\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 56\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 57\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 58\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 59\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 60\n@Makhmudov13_04')
    await message.reply_video(video=link11,caption='Unit 61\n@Makhmudov13_04')
    await message.reply_video(video=link12,caption='Unit 62\n@Makhmudov13_04')
    await message.reply_video(video=link13,caption='Unit 63\n@Makhmudov13_04')
    await message.reply_video(video=link14,caption='Unit 64\n@Makhmudov13_04')
    await message.reply_video(video=link15,caption='Unit 65\n@Makhmudov13_04')
    await message.reply_video(video=link16,caption='Unit 66\n@Makhmudov13_04')
    await message.reply_video(video=link17,caption='Unit 67\n@Makhmudov13_04')
    await message.reply_video(video=link18,caption='Unit 68\n@Makhmudov13_04')
    await message.reply_video(video=link19,caption='Unit 69\n@Makhmudov13_04')
    await message.reply_video(video=link20,caption='Unit 70\n@Makhmudov13_04')
@dp.message_handler(text='🔴 70-90 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/100'
    link2 = 'https://t.me/dddddddddddddddddddd122/101'
    link3 = 'https://t.me/dddddddddddddddddddd122/102'
    link4 = 'https://t.me/dddddddddddddddddddd122/103'
    link5 = 'https://t.me/dddddddddddddddddddd122/104'
    link6 = 'https://t.me/dddddddddddddddddddd122/105'
    link7 = 'https://t.me/dddddddddddddddddddd122/106'
    link8 = 'https://t.me/dddddddddddddddddddd122/107'
    link9 = 'https://t.me/dddddddddddddddddddd122/108'
    link10 = 'https://t.me/dddddddddddddddddddd122/109'
    link11 = 'https://t.me/dddddddddddddddddddd122/110'
    link12 = 'https://t.me/dddddddddddddddddddd122/111'
    link13 = 'https://t.me/dddddddddddddddddddd122/112'
    link14 = 'https://t.me/dddddddddddddddddddd122/113'
    link15 = 'https://t.me/dddddddddddddddddddd122/114'
    link16 = 'https://t.me/dddddddddddddddddddd122/115'
    link17 = 'https://t.me/dddddddddddddddddddd122/116'
    link18 = 'https://t.me/dddddddddddddddddddd122/117'
    link19 = 'https://t.me/dddddddddddddddddddd122/118'
    link20 = 'https://t.me/dddddddddddddddddddd122/119'
    await message.reply_video(video=link1, caption='Unit 71\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 72\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 73\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 74\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 75\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 76\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 77\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 78\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 79\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 80\n@Makhmudov13_04')
    await message.reply_video(video=link11,caption='Unit 81\n@Makhmudov13_04')
    await message.reply_video(video=link12,caption='Unit 82\n@Makhmudov13_04')
    await message.reply_video(video=link13,caption='Unit 83\n@Makhmudov13_04')
    await message.reply_video(video=link14,caption='Unit 84\n@Makhmudov13_04')
    await message.reply_video(video=link15,caption='Unit 85\n@Makhmudov13_04')
    await message.reply_video(video=link16,caption='Unit 86\n@Makhmudov13_04')
    await message.reply_video(video=link17,caption='Unit 87\n@Makhmudov13_04')
    await message.reply_video(video=link18,caption='Unit 88\n@Makhmudov13_04')
    await message.reply_video(video=link19,caption='Unit 89\n@Makhmudov13_04')
    await message.reply_video(video=link20,caption='Unit 90\n@Makhmudov13_04')

@dp.message_handler(text='🔴 90-100 lessons')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/121'
    link2 = 'https://t.me/dddddddddddddddddddd122/122'
    link3 = 'https://t.me/dddddddddddddddddddd122/123'
    link4 = 'https://t.me/dddddddddddddddddddd122/124'
    link5 = 'https://t.me/dddddddddddddddddddd122/125'
    link6 = 'https://t.me/dddddddddddddddddddd122/126'
    link7 = 'https://t.me/dddddddddddddddddddd122/127'
    link8 = 'https://t.me/dddddddddddddddddddd122/128'
    link9 = 'https://t.me/dddddddddddddddddddd122/129'
    link10 = 'https://t.me/dddddddddddddddddddd122/130'
    await message.reply_video(video=link1, caption='Unit 91\n@Makhmudov13_04')
    await message.reply_video(video=link2, caption='Unit 92\n@Makhmudov13_04')
    await message.reply_video(video=link3, caption='Unit 93\n@Makhmudov13_04')
    await message.reply_video(video=link4, caption='Unit 94\n@Makhmudov13_04')
    await message.reply_video(video=link5, caption='Unit 95\n@Makhmudov13_04')
    await message.reply_video(video=link6, caption='Unit 96\n@Makhmudov13_04')
    await message.reply_video(video=link7, caption='Unit 97\n@Makhmudov13_04')
    await message.reply_video(video=link8, caption='Unit 98\n@Makhmudov13_04')
    await message.reply_video(video=link9, caption='Unit 99\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 100\n@Makhmudov13_04')
    await message.reply_video(video=link10,caption='Unit 100\n@Makhmudov13_04')
@dp.message_handler(text='📚 Books')
async def bot_start(message: types.Message):
   await message.answer(text='Choice',reply_markup=books_button)
@dp.message_handler(text='📔 1 class')
async def bot_start(message: types.Message):
    await message.answer(text='Uzur bu sinf kitobi topilmadi boshqa sinf bilan harakat qilib koring')
@dp.message_handler(text='📔 2 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/131?single'
    link2 = 'https://t.me/dddddddddddddddddddd122/132?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
    await message.reply_document(document=link2,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 3 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/133?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 4 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/134?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 5 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/135?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 6 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/136?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 7 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/137?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 8 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/138?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 9 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/139?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 10 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/140?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 11 class')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/141?single'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📔 Maktab ingliz tili darsliklari')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/141?single'
    await message.answer(text='Choice',reply_markup=maktab_darsliklar_button)
@dp.message_handler(text='🇬🇧 Ingliz 🇬🇧')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/142'
    await message.reply_document(document=link1,caption='@Makhmudov13_04')
@dp.message_handler(text='📚 IELTS course')
async def bot_start(message: types.Message):
    await message.answer(text='Choice',reply_markup=ielts_button)
@dp.message_handler(text='☑️ Reading materials')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/146?single'
    link2 = 'https://t.me/dddddddddddddddddddd122/147?single'
    link3 = 'https://t.me/dddddddddddddddddddd122/148?single'
    link4 = 'https://t.me/dddddddddddddddddddd122/149?single'
    link5 = 'https://t.me/dddddddddddddddddddd122/150?single'
    link6 = 'https://t.me/dddddddddddddddddddd122/151?single'
    link7 = 'https://t.me/dddddddddddddddddddd122/152?single'
    link8 = 'https://t.me/dddddddddddddddddddd122/153?single'
    link9 = 'https://t.me/dddddddddddddddddddd122/154?single'
    link10 = 'https://t.me/dddddddddddddddddddd122/156?single'
    link11 = 'https://t.me/dddddddddddddddddddd122/157?single'
    link12 = 'https://t.me/dddddddddddddddddddd122/158?single'
    link13 = 'https://t.me/dddddddddddddddddddd122/159?single'
    link14 = 'https://t.me/dddddddddddddddddddd122/160?single'
    link15 = 'https://t.me/dddddddddddddddddddd122/161?single'
    link16 = 'https://t.me/dddddddddddddddddddd122/162?single'
    link17 = 'https://t.me/dddddddddddddddddddd122/163?single'
    link18 = 'https://t.me/dddddddddddddddddddd122/164?single'
    link19 = 'https://t.me/dddddddddddddddddddd122/165?single'
    link20 = 'https://t.me/dddddddddddddddddddd122/166?single'
    await message.reply_document(document=link1, caption='@Makhmudov13_04')
    await message.reply_document(document=link2, caption='@Makhmudov13_04')
    await message.reply_document(document=link3, caption='@Makhmudov13_04')
    await message.reply_document(document=link4, caption='@Makhmudov13_04')
    await message.reply_document(document=link5, caption='@Makhmudov13_04')
    await message.reply_document(document=link6, caption='@Makhmudov13_04')
    await message.reply_document(document=link7, caption='@Makhmudov13_04')
    await message.reply_document(document=link8, caption='@Makhmudov13_04')
    await message.reply_document(document=link9, caption='@Makhmudov13_04')
    await message.reply_document(document=link10, caption='@Makhmudov13_04')
    await message.reply_document(document=link11, caption='@Makhmudov13_04')
    await message.reply_document(document=link12, caption='@Makhmudov13_04')
    await message.reply_document(document=link13, caption='@Makhmudov13_04')
    await message.reply_document(document=link14, caption='@Makhmudov13_04')
    await message.reply_document(document=link15, caption='@Makhmudov13_04')
    await message.reply_document(document=link16, caption='@Makhmudov13_04')
    await message.reply_document(document=link17, caption='@Makhmudov13_04')
    await message.reply_document(document=link18, caption='@Makhmudov13_04')
    await message.reply_document(document=link19, caption='@Makhmudov13_04')
    await message.reply_document(document=link20, caption='@Makhmudov13_04')
@dp.message_handler(text='☑️ Writing materials')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/167?single'
    link2 = 'https://t.me/dddddddddddddddddddd122/168?single'
    link3 = 'https://t.me/dddddddddddddddddddd122/169?single'
    link4 = 'https://t.me/dddddddddddddddddddd122/170?single'
    link5 = 'https://t.me/dddddddddddddddddddd122/171?single'
    link6 = 'https://t.me/dddddddddddddddddddd122/172?single'
    link7 = 'https://t.me/dddddddddddddddddddd122/173?single'
    link8 = 'https://t.me/dddddddddddddddddddd122/174?single'
    link9 = 'https://t.me/dddddddddddddddddddd122/175?single'
    link10 = 'https://t.me/dddddddddddddddddddd122/176?single'
    link11 = 'https://t.me/dddddddddddddddddddd122/177?single'
    link12 = 'https://t.me/dddddddddddddddddddd122/178?single'
    link13 = 'https://t.me/dddddddddddddddddddd122/179?single'
    link14 = 'https://t.me/dddddddddddddddddddd122/180?single'
    link15 = 'https://t.me/dddddddddddddddddddd122/181?single'
    link16 = 'https://t.me/dddddddddddddddddddd122/182?single'
    link17 = 'https://t.me/dddddddddddddddddddd122/183?single'
    link18 = 'https://t.me/dddddddddddddddddddd122/184?single'
    link19 = 'https://t.me/dddddddddddddddddddd122/185?single'
    link20 = 'https://t.me/dddddddddddddddddddd122/186?single'
    await message.reply_document(document=link1, caption='@Makhmudov13_04')
    await message.reply_document(document=link2, caption='@Makhmudov13_04')
    await message.reply_document(document=link3, caption='@Makhmudov13_04')
    await message.reply_document(document=link4, caption='@Makhmudov13_04')
    await message.reply_document(document=link5, caption='@Makhmudov13_04')
    await message.reply_document(document=link6, caption='@Makhmudov13_04')
    await message.reply_document(document=link7, caption='@Makhmudov13_04')
    await message.reply_document(document=link8, caption='@Makhmudov13_04')
    await message.reply_document(document=link9, caption='@Makhmudov13_04')
    await message.reply_document(document=link10, caption='@Makhmudov13_04')
    await message.reply_document(document=link11, caption='@Makhmudov13_04')
    await message.reply_document(document=link12, caption='@Makhmudov13_04')
    await message.reply_document(document=link13, caption='@Makhmudov13_04')
    await message.reply_document(document=link14, caption='@Makhmudov13_04')
    await message.reply_document(document=link15, caption='@Makhmudov13_04')
    await message.reply_document(document=link16, caption='@Makhmudov13_04')
    await message.reply_document(document=link17, caption='@Makhmudov13_04')
    await message.reply_document(document=link18, caption='@Makhmudov13_04')
    await message.reply_document(document=link19, caption='@Makhmudov13_04')
    await message.reply_document(document=link20, caption='@Makhmudov13_04')
@dp.message_handler(text='☑️ Listening materials')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/187?single'
    link2 = 'https://t.me/dddddddddddddddddddd122/188?single'
    link3 = 'https://t.me/dddddddddddddddddddd122/189?single'
    link4 = 'https://t.me/dddddddddddddddddddd122/190?single'
    link5 = 'https://t.me/dddddddddddddddddddd122/191?single'
    link6 = 'https://t.me/dddddddddddddddddddd122/192?single'
    link7 = 'https://t.me/dddddddddddddddddddd122/193?single'
    link8 = 'https://t.me/dddddddddddddddddddd122/194?single'
    link9 = 'https://t.me/dddddddddddddddddddd122/195?single'
    link10 = 'https://t.me/dddddddddddddddddddd122/196?single'
    link11 = 'https://t.me/dddddddddddddddddddd122/197?single'
    link12 = 'https://t.me/dddddddddddddddddddd122/198?single'
    link13 = 'https://t.me/dddddddddddddddddddd122/199?single'
    link14 = 'https://t.me/dddddddddddddddddddd122/200?single'
    link15 = 'https://t.me/dddddddddddddddddddd122/201?single'
    link16 = 'https://t.me/dddddddddddddddddddd122/202?single'
    link17 = 'https://t.me/dddddddddddddddddddd122/203?single'
    link18 = 'https://t.me/dddddddddddddddddddd122/204?single'
    link19 = 'https://t.me/dddddddddddddddddddd122/205?single'
    link20 = 'https://t.me/dddddddddddddddddddd122/206?single'
    await message.reply_document(document=link1, caption='@Makhmudov13_04')
    await message.reply_document(document=link2, caption='@Makhmudov13_04')
    await message.reply_document(document=link3, caption='@Makhmudov13_04')
    await message.reply_document(document=link4, caption='@Makhmudov13_04')
    await message.reply_document(document=link5, caption='@Makhmudov13_04')
    await message.reply_document(document=link6, caption='@Makhmudov13_04')
    await message.reply_document(document=link7, caption='@Makhmudov13_04')
    await message.reply_document(document=link8, caption='@Makhmudov13_04')
    await message.reply_document(document=link9, caption='@Makhmudov13_04')
    await message.reply_document(document=link10, caption='@Makhmudov13_04')
    await message.reply_document(document=link11, caption='@Makhmudov13_04')
    await message.reply_document(document=link12, caption='@Makhmudov13_04')
    await message.reply_document(document=link13, caption='@Makhmudov13_04')
    await message.reply_document(document=link14, caption='@Makhmudov13_04')
    await message.reply_document(document=link15, caption='@Makhmudov13_04')
    await message.reply_document(document=link16, caption='@Makhmudov13_04')
    await message.reply_document(document=link17, caption='@Makhmudov13_04')
    await message.reply_document(document=link18, caption='@Makhmudov13_04')
    await message.reply_document(document=link19, caption='@Makhmudov13_04')
    await message.reply_document(document=link20, caption='@Makhmudov13_04')
@dp.message_handler(text='☑️ Speaking materials')
async def bot_start(message: types.Message):
    link1 = 'https://t.me/dddddddddddddddddddd122/207?single'
    link2 = 'https://t.me/dddddddddddddddddddd122/208?single'
    link3 = 'https://t.me/dddddddddddddddddddd122/209?single'
    link4 = 'https://t.me/dddddddddddddddddddd122/210?single'
    link5 = 'https://t.me/dddddddddddddddddddd122/211?single'
    link6 = 'https://t.me/dddddddddddddddddddd122/212?single'
    link7 = 'https://t.me/dddddddddddddddddddd122/213?single'
    link8 = 'https://t.me/dddddddddddddddddddd122/214?single'
    link9 = 'https://t.me/dddddddddddddddddddd122/215?single'
    link10 = 'https://t.me/dddddddddddddddddddd122/216?single'
    link11 = 'https://t.me/dddddddddddddddddddd122/217?single'
    link12 = 'https://t.me/dddddddddddddddddddd122/218?single'
    link13 = 'https://t.me/dddddddddddddddddddd122/219?single'
    link14 = 'https://t.me/dddddddddddddddddddd122/220?single'
    link15 = 'https://t.me/dddddddddddddddddddd122/221?single'
    link16 = 'https://t.me/dddddddddddddddddddd122/222?single'
    link17 = 'https://t.me/dddddddddddddddddddd122/223?single'
    link18 = 'https://t.me/dddddddddddddddddddd122/224?single'
    link19 = 'https://t.me/dddddddddddddddddddd122/225?single'
    link20 = 'https://t.me/dddddddddddddddddddd122/226?single'
    await message.reply_document(document=link1, caption='@Makhmudov13_04')
    await message.reply_document(document=link2, caption='@Makhmudov13_04')
    await message.reply_document(document=link3, caption='@Makhmudov13_04')
    await message.reply_document(document=link4, caption='@Makhmudov13_04')
    await message.reply_document(document=link5, caption='@Makhmudov13_04')
    await message.reply_document(document=link6, caption='@Makhmudov13_04')
    await message.reply_document(document=link7, caption='@Makhmudov13_04')
    await message.reply_document(document=link8, caption='@Makhmudov13_04')
    await message.reply_document(document=link9, caption='@Makhmudov13_04')
    await message.reply_document(document=link10, caption='@Makhmudov13_04')
    await message.reply_document(document=link11, caption='@Makhmudov13_04')
    await message.reply_document(document=link12, caption='@Makhmudov13_04')
    await message.reply_document(document=link13, caption='@Makhmudov13_04')
    await message.reply_document(document=link14, caption='@Makhmudov13_04')
    await message.reply_document(document=link15, caption='@Makhmudov13_04')
    await message.reply_document(document=link16, caption='@Makhmudov13_04')
    await message.reply_document(document=link17, caption='@Makhmudov13_04')
    await message.reply_document(document=link18, caption='@Makhmudov13_04')
    await message.reply_document(document=link19, caption='@Makhmudov13_04')
    await message.reply_document(document=link20, caption='@Makhmudov13_04')
