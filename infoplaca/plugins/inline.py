import re
from datetime import datetime as l

from pyrogram import Client
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from config import PLATES_ENDPOINT

from ..bot_strings import template
from ..utils import hc


@Client.on_inline_query()
async def inline(c: Client, m: InlineQuery):
    regex_m = r"((^| |\n)([a-zA-Z]{3}[0-9]{1}[a-zA-Z0-9][0-9]{2})( |\n|$))"
    if re.search(regex_m, m.query):
        pr = re.compile(regex_m)
        array_pl = pr.search(m.query)
        plac = array_pl[1]
        plate = re.sub("[^a-zA-Z0-9]", "", plac)

        r = await hc.get(PLATES_ENDPOINT.format(plate=plate))
        rjson = r.json()

        if rjson["codigoRetorno"] == 98:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title=f"⚠️ {rjson['mensagemRetorno']}",
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            message_text=f"⚠️ <b>{rjson['mensagemRetorno']}.</b>",
                            parse_mode="HTML",
                        ),
                    )
                ]
            )

        else:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title=f"Resultado para: {plate.upper()}",
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            str(
                                template.format(
                                    l.now().strftime("%d/%m/%Y às %H:%M:%S"),
                                    plate.upper(),
                                    rjson["chassi"],
                                    rjson["modelo"],
                                    rjson["cor"].upper(),
                                    rjson["ano"],
                                    rjson["municipio"].upper(),
                                    rjson["uf"],
                                    rjson["situacao"],
                                )
                            ),
                            parse_mode="HTML",
                        ),
                    )
                ]
            )
