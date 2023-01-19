from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup


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

    await m.edit_message_text(
        """Ajude no desenvolvimento e manutenção de nossos projetos.

Qualquer valor nos ajuda! 👋🤖""",
        reply_markup=keyboard,
    )


@Client.on_callback_query(filters.regex(r"gpix"))
async def xipg(c: Client, m: CallbackQuery):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🗑 Apagar mensagem", callback_data="delete")]
        ]
    )

    await m.message.reply_photo("#", caption="#", reply_markup=keyboard)


@Client.on_callback_query(filters.regex(r"delete"))
async def eteled(c: Client, m: CallbackQuery):
    await m.message.delete()
