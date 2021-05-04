from pyrogram import Client, filters
from pyrogram.types import (
        InlineKeyboardMarkup,
        InlineKeyboardButton)

from strin import strt, hlp
from daba import db, cursor
import sqlite3




def add_user(user_id):
    try:
        cursor.execute(
            """INSERT INTO users(user_id) VALUES (?)""", (user_id,)
)
    except sqlite3.IntegrityError:
        pass      
    db.commit()


# START COMMAND
@Client.on_message(filters.command("start", ["/", "!"]))
async def start(c, m):
    add_user(user_id=m.from_user.id)
    keybaard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                            text="🔎 Consulte inline", switch_inline_query_current_chat=""
                    )
                ]
            ]
        )
    await m.reply_text(strt, reply_markup=keybaard)
    
    
# HELP COMMAND
@Client.on_message(filters.command("help", ["/", "!"]))
async def help(c, m):
    keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                            text="💵 Colabore", callback_data="donate"
                    )
                ],
                [
                    InlineKeyboardButton(
                            text="💻 Meu desenvolvedor", url="t.me/khaledsecond"
                    )
                ]
            ]
        )
    await m.reply_text(hlp, reply_markup=keyboard)