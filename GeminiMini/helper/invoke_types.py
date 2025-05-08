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

from config import *
from google import genai
from google.genai import types as gen_types

def ini_client_gemini():
    return genai.Client(api_key=GOOGLE_API_KEY)

def setting_system_prompt_in_gemini(system_instruction: str):
    return gen_types.GenerateContentConfig(
        system_instruction=system_instruction,
        response_mime_type="text/plain",
        temperature=0,
        top_p=0.95,
        top_k=20,
        candidate_count=1,
        seed=5,
        max_output_tokens=4096,
        stop_sequences=['STOP!'],
        presence_penalty=0.0,
        frequency_penalty=0.0
    )
