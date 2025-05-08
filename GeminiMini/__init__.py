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

import asyncio
import logging
import time
import os
import pyrogram
from datetime import datetime as dt

from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *
from pyrogram.raw.all import layer

from config import *
from GeminiMini.database import db
from GeminiMini.helper.logger import LOGS

class GeminiMiniClient(Client):
    def __init__(self, loop=None):
        self.loop = loop or asyncio.get_event_loop()

        super().__init__(
            "GeminiMini",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=300,
            plugins=dict(root="GeminiMini.plugins"),
            sleep_threshold=180,
        )
        self._db = db

    async def start(self):
        try:
            await super().start()
        except FloodWait as e:
            LOGS.info(f"FloodWait: {str(e)}")
            await asyncio.sleep(e.value)

        self.start_time = time.time()
        LOGS.info(
            "Gemini Mini running with Pyrogram v%s (Layer %s) started on @%s. Hi!",
            pyrogram.__version__,
            layer,
            self.me.username,
        )
    async def stop(self):
        try:
            await super().stop()
            LOGS.warning("Gemini Mini stopped, Bye!")
        except ConnectionError:
            LOGS.warning("Gemini Mini is already terminated")
