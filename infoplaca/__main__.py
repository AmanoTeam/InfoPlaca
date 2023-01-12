import asyncio

from pyrogram import Client, idle

from config import API_HASH, API_ID, TOKEN


async def main():
    async with Client(
        "bot", API_ID, API_HASH, bot_token=TOKEN, plugins=dict(root="infoplaca.plugins")
    ):
        await idle()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
