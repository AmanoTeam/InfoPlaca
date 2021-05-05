from pyrogram import Client, idle
from configs import API_ID, API_HASH, TOKEN

import asyncio


async def main():
    await client.start()
    await idle()


client = Client("bot", API_ID, API_HASH, bot_token=TOKEN, plugins=dict(root="plugins"))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
