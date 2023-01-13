from datetime import datetime as l

import httpx
from pyrogram import Client, filters
from pyrogram.types import Message

from config import PLATES_ENDPOINT

from ..bot_strings import template
from ..utils import PLATE_REGEX, hc


@Client.on_message(filters.regex(PLATE_REGEX))
async def plate_search(c: Client, m: Message):
    plate: str = m.matches[0].group(1).upper()

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
        await m.reply_text(
            template.format(
                l.now().strftime("%d/%m/%Y às %H:%M:%S"),
                plate,
                rjson["chassi"],
                rjson["modelo"],
                rjson["cor"].upper(),
                rjson["ano"],
                rjson["municipio"].upper(),
                rjson["uf"],
                rjson["situacao"],
            ),
            quote=True,
        )
