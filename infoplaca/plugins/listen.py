import re
from datetime import datetime as l

from pyrogram import Client, filters
from pyrogram.types import Message

from config import PLATES_ENDPOINT

from ..bot_strings import template
from ..utils import hc

pattern = "((^| |\n)([a-z]{3}-?[0-9][a-z0-9][0-9]{2})( |\n|$))"


@Client.on_message(filters.regex(pattern))
async def listen(c: Client, m: Message):
    p = re.compile(pattern)
    q = p.search(m.text)
    r = q[1]
    plate = re.sub("[^a-zA-Z0-9]", "", r).upper()

    r = await hc.get(PLATES_ENDPOINT.format(plate=plate))
    rjson = r.json()

    if rjson["codigoRetorno"] == 98:
        await m.reply_text(
            f"⚠️ <b>{rjson['mensagemRetorno']}.</b>", quote=True, parse_mode="HTML"
        )

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
            parse_mode="HTML",
        )
