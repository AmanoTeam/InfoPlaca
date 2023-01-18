import httpx
from pyrogram import Client, filters
from pyrogram.types import Message

from config import PLATES_ENDPOINT

from ..utils import PLATE_REGEX, format_plate_info, hc


@Client.on_message(filters.regex(PLATE_REGEX) & ~filters.via_bot)
async def plate_search(c: Client, m: Message):
    plate: str = m.matches[0].group(1).upper().replace("-", "")

    try:
        r = await hc.get(PLATES_ENDPOINT.format(plate=plate))
        rjson = r.json()
    except httpx.HTTPError as e:
        await m.reply_text(
            f"⚠️ <b>Ocorreu um erro ao consultar esta placa, tente novamente mais tarde.</b>\n\n{e}",
            quote=True,
        )
        return

    if rjson["codigoRetorno"] == 98:
        await m.reply_text(f"⚠️ <b>{rjson['mensagemRetorno']}.</b>", quote=True)

    else:
        await m.reply_text(format_plate_info(rjson), quote=True)
