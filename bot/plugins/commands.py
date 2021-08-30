#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = "@MF_OFFICIAL"
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>🤭 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭\n\nനിങ്ങൾക് സിനിമകൾ വേണോ? അതിനായി ആദ്യം നിങ്ങൾ ചെയ്യേണ്ടത് ഞങ്ങളുടെ മെയിൻ ചാനലിൽ ജോയിൻ ആവുക എന്നതാണ്🤭... 😁\n\nJoin ചെയതത്തിനു ശേഷം വീണ്ടും ബോട്ട് /start ആക്കൂ AND FEEL THE MAGIC.😁</b>",
                reply_markup=InlineKeyboardMarkup([
                    [ InlineKeyboardButton(text=" 🤭JOIN OUR CHANNEL🤭 ", url=f"https://t.me/MF_OFFICIAL")]
              ])
            )
            return
        except Exception:
            await update.reply_text("Something Wrong. Contact my Support Group")
            return
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = "<b>👉 കൂടുതൽ സിനിമകൾക്കും മറ്റു വിവരങ്ങൾക്കുമായി ഞങ്ങളുടെ Group ൽ ജോയിൻ ചെയ്യൂ🌟\n\n༺ ──•◈•─ ─•◈•──༻ \nChannel🌐➧ @MF_UPDATES  \n👥➧ @MF_CHATGROUP</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    'CHANNEL🤪', url="https://t.me/MF_MOVIES1"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('🕵️‍♂️ ʙᴏᴛ ᴏᴡɴᴇʀ 🕵️‍♂️ ', url='https://t.me/JINN_OFF_TELEGRAM'),
        InlineKeyboardButton('🎻 ɢʀᴏᴜᴘ 🎻', url ='https://t.me/MF_CHATGROUP')
    ],[
        InlineKeyboardButton('🍿ᴊᴏɪɴ ᴏᴜʀ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ🍿', url='https://t.me/MF_OFFICIAL')
        
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/98c40bda1c03c514aea97.jpg",
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/98c40bda1c03c514aea97.jpg",
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
