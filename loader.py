from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data import config
from data.config import DB_HOST, DB_NAME, DB_PASS, DB_USER
from aiogram import Bot, types, Dispatcher

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}")

local_session = sessionmaker(autoflush=False, autocommit=False, bind=engine)

db = local_session()

Base = declarative_base()
