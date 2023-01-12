from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from ..bot_strings import hlp, strt
from ..database import add_user


# START COMMAND
@Client.on_message(filters.command("start", ["/", "!"]))
async def start(c: Client, m: Message):
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
async def help(c: Client, m: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💵 Colabore", callback_data="donate")],
            [InlineKeyboardButton(text="💻 Meu desenvolvedor", url="t.me/khaledsecond")],
        ]
    )
    await m.reply_text(hlp, reply_markup=keyboard)
