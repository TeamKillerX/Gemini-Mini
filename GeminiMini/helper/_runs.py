#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2020-2025 (c) Randy W @xtdevs, @xtsea
#
# from : https://github.com/TeamKillerX
# Channel : @RendyProjects
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import asyncio
import traceback
from pyrogram import idle
from contextlib import closing, suppress

from GeminiMini import GeminiMiniClient
from GeminiMini.helper.logger import LOGS
from GeminiMini.database import db

loop = asyncio.get_event_loop()

async def shutdown(loop):
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    for task in tasks:
        task.cancel()
    with suppress(asyncio.CancelledError):
        await asyncio.gather(*tasks, return_exceptions=True)
    LOGS.info("Application shutdown complete")

async def main_completed():
    try:
        await db.connect()
        _new_bots = GeminiMiniClient(loop=loop)
        await _new_bots.start()
        LOGS.info("Application startup complete")
        await idle()

    except Exception as e:
        LOGS.critical(f"Fatal error: {str(e)}")
        traceback.print_exc()
    finally:
        await shutdown(asyncio.get_event_loop())
