from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

ingliz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="To be fe'llari"),
            KeyboardButton(text='Zamonlar'),
        ],
        [
            KeyboardButton(text="Modal fe'llar"),
            KeyboardButton(text="Qo'shma gaplar")
        ],
        [
            KeyboardButton(text='Passive voice')
        ],
        [
            KeyboardButton(text='Reported speech')
        ],
        [
            KeyboardButton(text='🔴 Red Raymond Morphy lessons'),
            KeyboardButton(text='📚 Books')
        ],
        [
            KeyboardButton(text='📚 IELTS course'),
        ],
        [
            KeyboardButton(text='Tag questions')
        ],
        [
            KeyboardButton(text='🧑‍💻 Bot admini'),
            KeyboardButton(text='✍️ Fikr bildirish')
        ],
        [
            KeyboardButton(text='Reklama')
        ]
    ],resize_keyboard=True
)
ortga_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='◀️Ortga')
        ]
    ],resize_keyboard=True
)
tobe_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Am,is,are'),
            KeyboardButton(text='Was,were'),
            KeyboardButton(text='Will,Shall')
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
zamonlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Past tenses')
        ],
        [
            KeyboardButton(text='Present tenses')
        ],
        [
            KeyboardButton(text='Future tenses')
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
modal_fel_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Can'),
            KeyboardButton(text='May might')
        ],
        [
            KeyboardButton(text='Should'),
            KeyboardButton(text='(be) able to')
        ],
        [
            KeyboardButton(text='Must'),
            KeyboardButton(text='Have to')
        ],
        [
            KeyboardButton(text='Need'),
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
qoshma_gap_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Ifli gaplar'),
            KeyboardButton(text='Wishli gaplar')
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
passive_button = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Passive'),
            KeyboardButton(text='If it said that....,He is said that'),
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
reported_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='He is said that....'),
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
past_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Past simple'),
        ],
        [
            KeyboardButton(text='Past perfect')
        ],
        [
            KeyboardButton('Past continuous')
        ],
        [
            KeyboardButton(text='🔙 Go back'),
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
present_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Present simple')
        ],
        [
            KeyboardButton(text='Present continuous')
        ],
        [
            KeyboardButton(text='Present Perfect')
        ],
        [
            KeyboardButton(text='🔙 Go back'),
            KeyboardButton(text='🏠 Main menu')
        ]
        ],resize_keyboard=True
)
futere_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Future simple')
        ],
        [
            KeyboardButton(text='Future continious')
        ],
        [
            KeyboardButton(text='Future Perfect')
        ],
        [
            KeyboardButton(text='🔙 Go back'),
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
qizil_morfy_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🔴 1-5 lessons'),
            KeyboardButton(text='🔴 5-10lessons')
        ],
        [
            KeyboardButton(text='🔴 10-15 lessons'),
            KeyboardButton(text='🔴 15-20 lessons')
        ],
        [
            KeyboardButton(text='🔴 20-30 lessons'),
            KeyboardButton(text='🔴 30-40 lessons'),
            KeyboardButton(text='🔴 40-50 lessons'),
        ],
        [
            KeyboardButton(text='🔴 50-70 lessons'),
            KeyboardButton(text='🔴 70-90 lessons')
        ],
        [
            KeyboardButton(text='🔴 90-100 lessons'),
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)
books_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📔 Maktab ingliz tili darsliklari'),
            KeyboardButton(text='🇬🇧 Ingliz 🇬🇧'),
        ],
        [
            KeyboardButton(text='Ortga')
        ]

    ],resize_keyboard=True
)
maktab_darsliklar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📔 1 class'),
            KeyboardButton(text='📔 2 class'),
            KeyboardButton(text='📔 3 class')
        ],
        [
            KeyboardButton(text='📔 4 class'),
            KeyboardButton(text='📔 5 class'),
            KeyboardButton(text='📔 6 class')
        ],
        [
            KeyboardButton(text='📔 7 class'),
            KeyboardButton(text='📔 8 class'),
            KeyboardButton(text='📔 9 class')
        ],
        [
            KeyboardButton(text='📔 10 class'),
            KeyboardButton(text='📔 11 class'),
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True
)

ielts_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='☑️ Reading materials'),
            KeyboardButton(text='☑️ Writing materials')
        ],
        [
            KeyboardButton(text='☑️ Listening materials'),
            KeyboardButton(text='☑️ Speaking materials')
        ],
        [
            KeyboardButton(text='🏠 Main menu')
        ]
    ],resize_keyboard=True

)
