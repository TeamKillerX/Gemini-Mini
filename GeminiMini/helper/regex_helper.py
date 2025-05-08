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

import re

blacklist_patterns = [
    r"\bkill\s*yourself\b",
    r"\bi['’]?ll\s*rape\s*you\b",
    r"\bhate\s*speech\b",
    r"\bbomb\s*threat\b",
    r"\bterrorist\b",
    r"\bgore\s*content\b",
    r"\bchild\s*abuse\b",
    r"\bracist\s*slur\b",
    r"\bdeepfake\s*porn\b",
    r"\bnude\s*minors\b",
    r"\bsuicide\s*tutorial\b",
    r"\bhow\s*to\s*make\s*a\s*bomb\b",
    r"\billegal\s*weapon\b",
    r"\bschool\s*shooting\b",
    r"\bdeath\s*threat\b",
]

def is_blacklisted_english(text: str) -> bool:
    for pattern in blacklist_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def regex_match_string(pattern, text, is_match=False, is_findall=False):
    if is_match:
        return re.match(pattern, text, re.IGNORECASE)
    if is_findall:
        return re.findall(pattern, text, re.IGNORECASE)
    return re.match(pattern, text)
