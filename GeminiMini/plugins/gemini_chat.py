#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2019-2025 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import *
from pyrogram.types import *

from GeminiMini.helper.invoke_types import *
from GeminiMini.helper.logger import LOGS

gen = ini_client_gemini()

@Client.on_message(
    filters.private
    & filters.command(["start"])
    & ~filters.forwarded
)
async def startcmd(client, message):
    await client._db.addstart.update_one(
        {"bot_id": client.me.id},
        {"$addToSet": {"user_id": message.from_user.id}},
        upsert=True
    )
    return await message.reply_text(
       "Type anything to begin." 
    )

@Client.on_message(
    filters.text
    & filters.private
    & ~filters.command(["start"])
    & ~filters.forwarded
)
async def gemini_mini_talk(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        if message.reply_to_message.from_user.id != client.me.id:
            return
    if message.text:
        query = message.text.strip()
        try:
            response = await gen.aio.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=query,
                config=setting_system_prompt_in_gemini(
                    "You are my name cat coding and friends, multi languages"
                )
            )
            if response.text == "":
                return

            if len(response.text) > 4096:
                with open("output_chat", "w") as f:
                    f.write(response.text)
                await message.reply_document("output_chat")
                return
            else:
                await message.reply_text(
                    response.text,
                    disable_web_page_preview=True
                )
                return
        except Exception as e:
            LOGS.error(f"Error request: {str(e)}")
            await message.reply_text("Server busy try again later")
