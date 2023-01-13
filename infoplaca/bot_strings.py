# START COMMAND
strt = """Digite a placa ou clique no botão abaixo."""


# HELP COMMAND
hlp = """Olá 👋, aqui é a área de ajuda do <b>InfoPlaca</b>.

ℹ️ <b>Informações básicas:</b>
Para consultar uma placa envie no formato: <code>ABC-1234</code> ou <code>ABC1234</code>.
Também disponível a consulta no formato <b>MERCOSUL</b>: <code>ABC1A23</code>
<i>*Disponível para qualquer veículo.</i>

O uso também pode ser via inline, digite: <code>@InfoPlacaBot PLACA</code> no campo de texto.
<i>*Atalho na mensagem de start.</i>



🤖 Quer colaborar nossos projetos? Clique no botão abaixo e apoie o meu desenvolvimento!"""


# DONATE COMMAND
donate = """Ajude no desenvolvimento e manutenção de nossos projetos.

Qualquer valor nos ajuda! 👋🤖"""


# TEMPLATE TO INSERT REQUEST INFO
template = """ℹ️ <b>Informações da Placa</b>
📆 <i>{}</i>

<b>Placa:</b> <code>{}</code>
<b>Chassi:</b> <code>***{}</code>
<b>Modelo:</b> <code>{}</code>
<b>Cor:</b> <code>{}</code>
<b>Ano:</b> <code>{}</code>
<b>Cidade:</b> <code>{}-{}</code>
<b>Situação:</b> <code>{}</code>

@InfoPlacabot"""
