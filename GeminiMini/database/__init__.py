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

import os
import time
from datetime import datetime as dt

from motor import motor_asyncio
from motor.core import AgnosticClient

from config import *
from GeminiMini.helper.logger import LOGS


class Database:
    def __init__(self, uri: str) -> None:
        self.client: AgnosticClient = motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self.client["Gemini"]
        self.addstart = self.db["broadcast_list"]
        self.backup_chatbot = self.db["google_genai"]

    async def connect(self):
        try:
            await self.client.admin.command("ping")
            LOGS.info(f"Database Connected mongodb!")
        except Exception as e:
            LOGS.info(f"DatabaseErr: {e} ")
            quit(1)

    async def _close(self):
        await self.client.close()

    def get_datetime(self) -> str:
        return dt.now().strftime("%d/%m/%Y - %H:%M")

db = Database(MONGO_URL)
