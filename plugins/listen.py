from bot_strings import template
from configs import PROXY
from datetime import datetime as l
from pyrogram import Client, filters

import re
import httpx


pattern = "((^| |\n)([a-z]{3}-?[0-9][a-z0-9][0-9]{2})( |\n|$))"


@Client.on_message(filters.regex(pattern))
async def listen(c, m):
    p = re.compile(pattern)
    q = p.search(m.text)
    r = q.group(1)
    s = re.sub("[^a-zA-Z0-9]", "", r).upper()
    with httpx.Client(proxies=PROXY) as cli:
        v = cli.get(f"#").json()

    if v["codigoRetorno"] == 98:
        await m.reply_text(
            f"⚠️ <b>{v['mensagemRetorno']}.</b>", quote=True, parse_mode="HTML"
        )

    else:
        await m.reply_text(
            template.format(
                l.now().strftime("%d/%m/%Y às %H:%M:%S"),
                s,
                v["chassi"],
                v["modelo"],
                v["cor"].upper(),
                v["ano"],
                v["municipio"].upper(),
                v["uf"],
                v["situacao"],
            ),
            quote=True,
            parse_mode="HTML",
        )
