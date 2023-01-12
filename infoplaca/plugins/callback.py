from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from ..bot_strings import donate, hlp


@Client.on_callback_query(filters.regex(r"donate"))
async def etanod(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="💵 PicPay", url="#"),
                InlineKeyboardButton(text="💵 PayPal", url="#"),
            ],
            [InlineKeyboardButton(text="💵 Pix", callback_data="gpix")],
            [InlineKeyboardButton(text="◀️ Voltar", callback_data="help")],
        ]
    )
    await m.edit_message_text(donate, reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"help"))
async def pleh(c: Client, m: CallbackQuery):
    keyvoard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="💵 Colabore", callback_data="donate")],
            [InlineKeyboardButton(text="💻 Meu desenvolvedor", url="t.me/khaledsecond")],
            [
                InlineKeyboardButton(
                    text="🔎 Consulte inline", switch_inline_query_current_chat=""
                )
            ],
        ]
    )
    await m.edit_message_text(hlp, reply_markup=keyvoard)


@Client.on_callback_query(filters.regex(r"gpix"))
async def xipg(c: Client, m: CallbackQuery):
    keybaard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗑 Apagar mensagem", callback_data="delete")]
        ]
    )
    await c.send_photo(m.message.chat.id, photo="#", caption="#", reply_markup=keybaard)


@Client.on_callback_query(filters.regex(r"delete"))
async def eteled(c: Client, m: CallbackQuery):
    await c.delete_messages(m.message.chat.id, m.message.message_id)
