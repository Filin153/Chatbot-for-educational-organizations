import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def generate_docs_butt():
    docs_butt = InlineKeyboardMarkup()
    all_file = os.listdir("file")
    for i in all_file:
        docs_butt.add(InlineKeyboardButton(f"{i.split('.')[0]}", callback_data=f"send_file:{all_file.index(i)}"))
    return docs_butt
