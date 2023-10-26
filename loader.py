from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from data import config
from aiogram import Bot, Dispatcher, types

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

engine = create_engine('sqlite:///sqlite3.db')

local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

db = local_session()

Base = declarative_base()
