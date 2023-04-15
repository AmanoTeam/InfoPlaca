import re
from datetime import datetime

import httpx

hc = httpx.AsyncClient()

PLATE_REGEX = re.compile(
    r"(?:^| |\n)(([a-z]{3})-?([0-9][a-z0-9][0-9]{2}))(?: |\n|$)", re.IGNORECASE
)


def format_plate(plate: str) -> str:
    groups = re.search(PLATE_REGEX, plate).groups()
    if groups[2].isnumeric():
        return f"{groups[1]}-{groups[2]}"
    return f"{groups[1]}{groups[2]}"


def format_plate_info(info: dict) -> str:
    try:
        date = datetime.fromisoformat(info["data"]).strftime("%d/%m/%Y às %H:%M:%S")
    except ValueError:
        date = info["data"]

    return """ℹ️ <b>Informações da Placa</b>
📆 <i>Informações atualizadas em {}</i>

<b>Placa:</b> <code>{}</code>
<b>Chassi:</b> <code>{}</code>
<b>Modelo:</b> <code>{}</code>
<b>Cor:</b> <code>{}</code>
<b>Ano/Modelo:</b> <code>{}/{}</code>
<b>Cidade:</b> <code>{} - {}</code>
<b>Situação:</b> <code>{}</code>

@InfoPlacaBot""".format(
        date,
        format_plate(info["placa"]),
        info["chassi"].rjust(17, "*") if info["chassi"] else "Não informado",
        info["modelo"].title(),
        info["cor"].title(),
        info["ano"],
        info["anoModelo"],
        info["municipio"].title(),
        info["uf"],
        info["situacao"],
    )
