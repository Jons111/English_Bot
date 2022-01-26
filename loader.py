from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sqlite3
from data import config
from utils.db_api.baza import Database

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
d = Database(path_to_db="main.db")
db = sqlite3.connect('main.db',check_same_thread=False)
