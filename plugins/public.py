#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import asyncio
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import FloodWait
from config import Config
from translation import Translation

FILTER = Config.FILTER_TYPE
files_count = 0

#===================Run Function===================#

@Client.on_message(filters.private & filters.command(["run"]))
async def run(bot, message):
    global SKIP
    global FROM
    global TO
    global LIMIT
    if str(message.from_user.id) not in Config.OWNER_ID:
        return
    fromid = await bot.ask(message.chat.id, Translation.FROM_MSG)
    if fromid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    elif not fromid.text.startswith('@'):
        return await message.reply(Translation.USERNAME)
    toid = await bot.ask(message.chat.id, Translation.TO_MSG)
    if toid.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    skipno = await bot.ask(message.chat.id, Translation.SKIP_MSG)
    if skipno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    limitno = await bot.ask(message.chat.id, Translation.LIMIT_MSG)
    if limitno.text.startswith('/'):
        await message.reply(Translation.CANCEL)
        return
    buttons = [[
        InlineKeyboardButton('Yes', callback_data='start_public'),
        InlineKeyboardButton('No', callback_data='close_btn')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        text=Translation.DOUBLE_CHECK.format(fromid.text),
        reply_markup=reply_markup
    )
    SKIP = skipno.text
    FROM = fromid.text
    TO = toid.text
    LIMIT = limitno.text
    if re.match('-100\d+', TO):
        TO = int(TO)
