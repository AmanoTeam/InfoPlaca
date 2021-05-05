from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from string import template
from configs import PROXY
from datetime import datetime as l

import re
import httpx


@Client.on_inline_query()
async def inline(c, m):
    # PADRAO CONVENCIONAL
    regex_c = "(( |\n|^)[A-Za-z]{3}(( - )| |-)?[0-9]{4}( |\n|$))"
    if re.search(regex_c, m.query):
        p = re.compile(regex_c)
        array_placa = p.search(m.query)
        placa = array_placa.group(1)
        f = re.sub("[^a-zA-Z0-9]", "", placa)
        g = re.sub(r"([a-zA-Z]+)[- ]?(\d+)", r"\1-\2", f).upper()
        with httpx.Client(proxies=PROXY) as cli:
            h = cli.get(
                f"http://api.masterplaca.devplank.com/v51/placa/{f}/json"
            ).json()

        if h["codigoRetorno"] == 98:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title=f"⚠️ {h['mensagemRetorno']}",
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            message_text=f"⚠️ <b>{h['mensagemRetorno']}.</b>",
                            parse_mode="HTML",
                        ),
                    )
                ]
            )

        else:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title="Resultado para: " + g,
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            str(
                                template.format(
                                    l.now().strftime("%d/%m/%Y às %H:%M:%S"),
                                    g,
                                    h["chassi"],
                                    h["modelo"],
                                    h["cor"].upper(),
                                    h["ano"],
                                    h["municipio"].upper(),
                                    h["uf"],
                                    h["situacao"],
                                )
                            ),
                            parse_mode="HTML",
                        ),
                    )
                ]
            )

    else:
        pass

    # PADRAO MERCOSUL
    regex_m = r"((^| |\n)([a-zA-Z]{3}[0-9]{1}[a-zA-Z][0-9]{2})( |\n|$))"
    if re.search(regex_m, m.query):
        pr = re.compile(regex_m)
        array_pl = pr.search(m.query)
        plac = array_pl.group(1)
        p = re.sub("[^a-zA-Z0-9]", "", plac)
        with httpx.Client(proxies=PROXY) as cl:
            q = cl.get(f"http://api.masterplaca.devplank.com/v51/placa/{p}/json").json()

        if q["codigoRetorno"] == 98:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title=f"⚠️ {q['mensagemRetorno']}",
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            message_text=f"⚠️ <b>{q['mensagemRetorno']}.</b>",
                            parse_mode="HTML",
                        ),
                    )
                ]
            )

        else:
            await m.answer(
                [
                    InlineQueryResultArticle(
                        title="Resultado para: " + p.upper(),
                        thumb_url="https://piics.ml/i/015.png",
                        input_message_content=InputTextMessageContent(
                            str(
                                template.format(
                                    l.now().strftime("%d/%m/%Y às %H:%M:%S"),
                                    p.upper(),
                                    q["chassi"],
                                    q["modelo"],
                                    q["cor"].upper(),
                                    q["ano"],
                                    q["municipio"].upper(),
                                    q["uf"],
                                    q["situacao"],
                                )
                            ),
                            parse_mode="HTML",
                        ),
                    )
                ]
            )

    else:
        pass
