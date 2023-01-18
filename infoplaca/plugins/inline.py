import httpx
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from config import PLATES_ENDPOINT

from ..utils import PLATE_REGEX, format_plate, format_plate_info, hc


@Client.on_inline_query(filters.regex(PLATE_REGEX))
async def plate_search_inline(c: Client, m: InlineQuery):
    plate: str = m.matches[0].group(1).upper().replace("-", "")

    try:
        r = await hc.get(PLATES_ENDPOINT.format(plate=plate))
        rjson = r.json()
    except httpx.HTTPError as e:
        await m.answer(
            [
                InlineQueryResultArticle(
                    title="⚠️ Erro ao consultar",
                    thumb_url="https://piics.ml/i/015.png",
                    input_message_content=InputTextMessageContent(
                        message_text=f"⚠️ <b>Ocorreu um erro ao consultar esta placa, tente novamente mais tarde.</b>\n\n{e}",
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        inline_keyboard=[
                            [
                                InlineKeyboardButton(
                                    text="🔎 Tentar novamente",
                                    switch_inline_query_current_chat=plate,
                                )
                            ]
                        ]
                    ),
                )
            ],
            cache_time=0,
        )
        return

    if rjson["codigoRetorno"] == 98:
        await m.answer(
            [
                InlineQueryResultArticle(
                    title=f"⚠️ {rjson['mensagemRetorno']}",
                    thumb_url="https://piics.ml/i/015.png",
                    input_message_content=InputTextMessageContent(
                        message_text=f"⚠️ <b>{rjson['mensagemRetorno']}.</b>",
                    ),
                )
            ]
        )

    else:
        await m.answer(
            [
                InlineQueryResultArticle(
                    title=f"Resultado para: {format_plate(plate)}",
                    thumb_url="https://piics.ml/i/015.png",
                    input_message_content=InputTextMessageContent(
                        format_plate_info(rjson)
                    ),
                )
            ]
        )


@Client.on_inline_query()
async def empty_inline(c: Client, m: InlineQuery):
    await m.answer(
        [
            InlineQueryResultArticle(
                title="🔎 Insira uma placa para consultar via inline",
                thumb_url="https://piics.ml/i/015.png",
                input_message_content=InputTextMessageContent(
                    message_text="🔎 <b>Insira uma placa para consultar via inline</b>",
                ),
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(
                                text="🔎 Consulte inline",
                                switch_inline_query_current_chat="",
                            )
                        ]
                    ]
                ),
            )
        ],
        cache_time=0,
    )
