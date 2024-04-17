import asyncio

from Auput import app
from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from config import MUSIC_BOT_NAME, OWNER_USERNAME, SUPPORT_CHANNEL

@app.on_message(filters.command("alive", ["/", ".", "!"]))
async def kontolmasukmemek(client: Client, message: Message):
    await message.reply_video(
        video=f"https://graph.org/file/f4ef292ae52ed6f66cb95.jpg",
        caption=f"🥀 Hei {message.from_user.mention}\n\n I am {MUSIC_BOT_NAME}\n\n🔥 I am Fast and Powerful music player bot with some awesome features.\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
               [
            InlineKeyboardButton(
                text="ʜᴋꝛ · ᴀ ɪ ᴜ", url=f"https://t.me/{OWNER_USERNAME}"
            ),
            InlineKeyboardButton(
                text="ᴄʜᴀɴɴᴇʟ", url=f"{SUPPORT_CHANNEL}"
            ),
        ],
                [
                    InlineKeyboardButton(
                        "ᴄʟᴏsᴇ", callback_data="close"
                    )
                ],
            ]
        )
    )
