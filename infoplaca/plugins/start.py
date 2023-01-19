from typing import Union

from pyrogram import Client, filters
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

from ..database import add_user


# START COMMAND
@Client.on_message(filters.command("start", ["/", "!"]))
async def start(c: Client, m: Message):
    add_user(user_id=m.from_user.id)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔎 Consulte inline", switch_inline_query_current_chat=""
                )
            ]
        ]
    )
    await m.reply_text(
        "Digite a placa ou clique no botão abaixo.", reply_markup=keyboard
    )


# HELP COMMAND
@Client.on_callback_query(filters.regex(r"help"))
@Client.on_message(filters.command("help", ["/", "!"]))
async def pleh(c: Client, m: Union[CallbackQuery, Message]):
    send = m.edit_message_text if isinstance(m, CallbackQuery) else m.reply_text

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💵 Colabore", callback_data="donate")],
            [
                InlineKeyboardButton(
                    text="💻 Meu desenvolvedor", url="https://t.me/khaledsecond"
                )
            ],
            [
                InlineKeyboardButton(
                    text="🔎 Consulte inline", switch_inline_query_current_chat=""
                )
            ],
        ]
    )

    await send(
        """Olá 👋, aqui é a área de ajuda do <b>InfoPlaca</b>.

ℹ️ <b>Informações básicas:</b>
Para consultar uma placa, envie no formato <code>ABC-1234</code> ou <code>ABC1234</code> (Mercosul).
<i>*Disponível para qualquer veículo.</i>

O uso também pode ser via inline, digite: <code>@InfoPlacaBot PLACA</code> no campo de texto.
<i>*Atalho na mensagem de start.</i>



🤖 Quer colaborar nossos projetos? Clique no botão abaixo e apoie o meu desenvolvimento!""",
        reply_markup=keyboard,
    )
