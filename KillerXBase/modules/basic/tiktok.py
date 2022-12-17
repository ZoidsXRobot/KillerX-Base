import asyncio
from pyrogram.types import *
from pyrogram import *
from pyrogram import Client as ren
from pyrogram import Client
from KillerXBase.helper.cmd import *
from KillerXBase.helper.basic import *
from KillerXBase.helper.PyroHelpers import *

@ren.on_message(filters.command(["tt", "tiktok", "ig", "sosmed"], cmd) & filters.me)
async def tiktok(client: Client, message: Message):
    prik = await message.edit("`Processing . . .`")
    link = get_arg(message)
    bot = "thisvidbot"
    if link:
        try:
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
        except YouBlockedUser:
            await client.unblock_user(bot)
            tuyul = await client.send_message(bot, link)
            await asyncio.sleep(5)
            await tuyul.delete()
    async for tiktok in client.search_messages(
        bot, filter=enums.MessagesFilter.VIDEO, limit=1
    ):
        await asyncio.gather(
            prik.delete(),
            client.send_video(
                message.chat.id,
                sosmed.video.file_id,
                caption=f"**Upload by:** {client.me.mention}",
                reply_to_message_id=ReplyCheck(message),
            ),
        )
        await client.delete_messages(bot, 2)
