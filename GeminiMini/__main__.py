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
import logging
import sys

from uvloop import install
from contextlib import closing, suppress
from GeminiMini.helper._runs import *

loop = asyncio.get_event_loop()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram.syncer").setLevel(logging.WARNING)
logging.getLogger("pyrogram.client").setLevel(logging.WARNING)

if __name__ == "__main__":
    install()
    with closing(loop):
        with suppress(asyncio.CancelledError, KeyboardInterrupt):
            loop.run_until_complete(main_completed())

        loop.run_until_complete(asyncio.sleep(3))
        if not loop.is_closed():
            loop.close()
