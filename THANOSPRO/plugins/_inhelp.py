import asyncio
import html
import os
import re
import random
import sys

from math import ceil
from re import compile

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.events import InlineQuery, callbackquery
from telethon.sync import custom
from telethon.errors.rpcerrorlist import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from THANOSPRO.sql.gvar_sql import gvarstat
from . import *

rishu_row = Config.BUTTONS_IN_HELP
rishu_emoji = Config.EMOJI_IN_HELP
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"
LOG_GP = Config.LOGGER_ID
USER_BOT_WARN_ZERO = "Enough Of Your Flooding In My Master's PM!! \n\n**๐ซ Blocked and Reported**"

alive_txt = """{}\n
<b><i>๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐</b></i>
<b>Telethon โ</b>  <i>{}</i>
<b>ีัเธเธ เนเธฃ-ืงะณเน โ</b>  <i>{}</i>
<b>Uptime โ</b>  <i>{}</i>
<b>Abuse โ</b>  <i>{}</i>
<b>Sudo โ</b>  <i>{}</i>
"""

def button(page, modules):
    Row = rishu_row
    Column = 3

    modules = sorted([modul for modul in modules if not modul.startswith("_")])
    pairs = list(map(list, zip(modules[::2], modules[1::2])))
    if len(modules) % 2 == 1:
        pairs.append([modules[-1]])
    max_pages = ceil(len(pairs) / Row)
    pairs = [pairs[i : i + Row] for i in range(0, len(pairs), Row)]
    buttons = []
    for pairs in pairs[page]:
        buttons.append(
            [
                custom.Button.inline(f"{rishu_emoji} " + pair + f" {rishu_emoji}", data=f"Information[{page}]({pair})")
                for pair in pairs
            ]
        )

    buttons.append(
        [
            custom.Button.inline(
               f"โ Back {rishu_emoji}", data=f"page({(max_pages - 1) if page == 0 else (page - 1)})"
            ),
            custom.Button.inline(
               f"๐ฅ โ ๐ฅ", data="close"
            ),
            custom.Button.inline(
               f"{rishu_emoji} Next โ ", data=f"page({0 if page == (max_pages - 1) else page + 1})"
            ),
        ]
    )
    return [max_pages, buttons]


    modules = CMD_HELP
if Config.BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(InlineQuery)
    async def inline_handler(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        builder = event.builder
        result = None
        query = event.text
        auth = await clients_list()
        if event.query.user_id in auth and query == "THANOSPRO_help":
            rev_text = query[::-1]
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            a = gvarstat("HELP_PIC")
            if a:
                help_pic = a.split(" ")[0]
            else:
                help_pic = "https://telegra.ph/file/7eaaefe63542f68ab19f1.mp4"
            help_msg = f"ใ{rishu_mention}ใ\n\n๐ฉเผยฉ๐ผ๐๐๐๐๐๐เผ๐ชโฃโชผ `{len(CMD_HELP)}`\n๐ฉเผยฉ๐ฒ๐๐๐๐๐๐๐เผ๐ชโฃโชผโญ `{len(apn)}`\n๐ฉเผยฉPฮฑึาฝเผ๐ชโฃโชผ 1/{veriler[0]}"
            if help_pic == "DISABLE":
                result = builder.article(
                    f"Hey! Only use {hl}help please",
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic.endswith((".jpg", ".png")):
                result = builder.photo(
                    help_pic,
                    text=help_msg,
                    buttons=veriler[1],
                    link_preview=False,
                )
            elif help_pic:
                result = builder.document(
                    help_pic,
                    text=help_msg,
                    title="THANOSPRO Alive",
                    buttons=veriler[1],
                    link_preview=False,
                )
        elif event.query.user_id in auth and query == "alive":
            uptime = await get_time((time.time() - StartTime))
            alv_msg = gvarstat("ALIVE_MSG") or "ยปยปยป <b>ีัเธเธ เนเธฃืงะณเน ฮนั ฯะธโฮนะธั</b> ยซยซยซ"
            he_ll = alive_txt.format(alv_msg, tel_ver, rishu_ver, uptime, abuse_m, is_sudo)
            alv_btn = [
                [Button.url(f"{rishu_USER}", f"tg://openmessage?user_id={ultronceo}")],
                [Button.url("My Channel", f"https://t.me/{my_channel}"), 
                Button.url("My Group", f"https://t.me/{my_group}")],
            ]
            a = gvarstat("ALIVE_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/7eaaefe63542f68ab19f1.mp4"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    PIC,
                    text=he_ll,
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            elif PIC:
                result = builder.document(
                    PIC,
                    text=he_ll,
                    title="THANOSPRO Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )
            else:
                result = builder.article(
                    text=he_ll,
                    title="THANOSPRO Alive",
                    buttons=alv_btn,
                    link_preview=False,
                    parse_mode="HTML",
                )

        elif event.query.user_id in auth and query == "pm_warn":
            CSTM_PMP = gvarstat("CUSTOM_PMPERMIT") or "**You Have Trespassed To My Master's PM!\nThis Is Illegal And Regarded As Crime.**"
            rishu_FIRST = "**๐ฅ ีัเธเธ เนเธฃ-ืงะณเน Prรฎvรฃโ รฉ Sรชรงรผrรฏty Prรธโ รถรงรตl ๐ฅ**\n\nrishuo!! Welcome to {}'s PM. This is an automated message.\n\n{}".format(rishu_mention, CSTM_PMP)
            a = gvarstat("PMPERMIT_PIC")
            pic_list = []
            if a:
                b = a.split(" ")
                if len(b) >= 1:
                    for c in b:
                        pic_list.append(c)
                PIC = random.choice(pic_list)
            else:
                PIC = "https://telegra.ph/file/415251e40871963785155.jpg"
            if PIC and PIC.endswith((".jpg", ".png")):
                result = builder.photo(
                    file=PIC,
                    text=rishu_FIRST,
                    buttons=[
                        [custom.Button.inline("๐ Request Approval", data="req")],
                        [custom.Button.inline("๐ซ Block", data="heheboi")],
                        [custom.Button.inline("โ Curious", data="pmclick")],
                    ],
                    link_preview=False,
                )
            elif PIC:
                result = builder.document(
                    file=PIC,
                    text=rishu_FIRST,
                    title="THANOSPRO PM Permit",
                    buttons=[
                        [custom.Button.inline("๐ Request Approval", data="req")],
                        [custom.Button.inline("๐ซ Block", data="heheboi")],
                        [custom.Button.inline("โ Curious", data="pmclick")],
                    ],
                    link_preview=False,
                )
            else:
                result = builder.article(
                    text=rishu_FIRST,
                    title="THANOSPRO PM Permit",
                    buttons=[
                        [custom.Button.inline("๐ Request Approval", data="req")],
                        [custom.Button.inline("๐ซ Block", data="heheboi")],
                        [custom.Button.inline("โ Curious", data="pmclick")],
                    ],
                    link_preview=False,
                )
                
        elif event.query.user_id in auth and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"**โก สษษขษีผษaสส แดา ีัเธเธ เนเธฃืงะณเน โก**",
                buttons=[
                    [Button.url("๐ Repo ๐", "https://github.com/thanosuser/THANOS-PROS")],
                    [Button.url("THANOSPRO Netwprk", "https://t.me/thanospros")],
                ],
            )

        elif query.startswith("http"):
            part = query.split(" ")
            result = builder.article(
                "File uploaded",
                text=f"**File uploaded successfully to {part[2]} site.\n\nUpload Time : {part[1][:3]} second\n[โโโ โ]({part[0]})",
                buttons=[[custom.Button.url("URL", part[0])]],
                link_preview=True,
            )

        else:
            result = builder.article(
                "@thanospros",
                text="""**Hey! This is [ีัเธเธ เนเธฃ-ืงะณเน](https://t.me/thanospros) \nYou can know more about me from the links given below ๐**""",
                buttons=[
                    [
                        custom.Button.url("๐ฅ CHANNEL ๐ฅ", "https://t.me/thanospros"),
                        custom.Button.url("โก GROUP โก", "https://t.me/THANOSPRO_chat"),
                    ],
                    [
                        custom.Button.url("โจ REPO โจ", "https://github.com/thanosuser/THANOS-PROS"),
                        custom.Button.url("๐ฐ TUTORIAL ๐ฐ", "https://youtu.be/M2FQJq_sHp4"),
                    ],
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"pmclick")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "This is for Other Users..."
        else:
            reply_pop_up_alert = "๐ฐ This is ีัเธเธ เนเธฃ-ืงะณเน PM Security to keep away unwanted retards from spamming PM !!"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"req")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit("โ **Request Registered** \n\nMy master will now decide to look for your request or not.\n๐ Till then wait patiently and don't spam!!")
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(LOG_GP, f"#PM_REQUEST \n\nโ๏ธ You got a PM request from [{first_name}](tg://user?id={event.query.user_id}) !")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"heheboi")))
    async def on_pm_click(event):
        auth = await clients_list()
        if event.query.user_id in auth:
            reply_pop_up_alert = "This is for other users!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            await event.edit(f"As you wish. **BLOCKED !!**")
            await H1(functions.contacts.BlockRequest(event.query.user_id))
            target = await event.client(GetFullUserRequest(event.query.user_id))
            first_name = html.escape(target.user.first_name)
            if first_name is not None:
                first_name = first_name.replace("\u2060", "")
            await tbot.send_message(LOG_GP, f"#BLOCK \n\n**Blocked** [{first_name}](tg://user?id={event.query.user_id}) \nReason:- PM Self Block")


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"reopen")))
    async def reopn(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            current_page_number=0
            simp = button(current_page_number, CMD_HELP)
            veriler = button(0, sorted(CMD_HELP))
            apn = []
            for x in CMD_LIST.values():
                for y in x:
                    apn.append(y)
            await event.edit(
                f"ใ{rishu_mention}ใ\n\n๐ฉเผยฉ๐ผ๐๐๐๐๐๐เผ๐ชโฃโชผ `{len(CMD_HELP)}`\n๐ฉเผยฉ๐ฒ๐๐๐๐๐๐๐เผ๐ชโฃโชผโญ `{len(apn)}`\n๐ฉเผยฉPฮฑึาฝเผ๐ชโฃโชผ 1/{veriler[0]}",
                buttons=simp[1],
                link_preview=False,
            )
        else:
            reply_pop_up_alert = "You are not authorized to use me! \nยฉ ีัเธเธ เนเธฃ-ืงะณเน โข"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        if event.query.user_id in auth:
            veriler = custom.Button.inline(f"{rishu_emoji} Re-Open Menu {rishu_emoji}", data="reopen")
            await event.edit(f"**โ๏ธ ีัเธเธ เนเธฃ-ืงะณเน Mรชรฑรป Prรตvรฎdรชr รฌs รฑรดw รlรถsรซd โ๏ธ**\n\n**Bot Of :**  {rishu_mention}\n\n        [ยฉ๏ธ ีัเธเธ เนเธฃ-ืงะณเน โข๏ธ]({chnl_link})", buttons=veriler, link_preview=False)
        else:
            reply_pop_up_alert = "You are not authorized to use me! \nยฉ ีัเธเธ เนเธฃ-ืงะณเน โข"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
   

    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"page\((.+?)\)")))
    async def page(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        veriler = button(page, CMD_HELP)
        apn = []
        for x in CMD_LIST.values():
            for y in x:
                apn.append(y)
        if event.query.user_id in auth:
            await event.edit(
                f"ใ{rishu_mention}ใ\n\n๐ฉเผยฉ๐ผ๐๐๐๐๐๐เผ๐ชโฃโชผ `{len(CMD_HELP)}`\n๐ฉเผยฉ๐ฒ๐๐๐๐๐๐๐เผ๐ชโฃโชผโญ `{len(apn)}`\n๐ฉเผยฉPฮฑึาฝเผ๐ชโฃโชผ 1/{veriler[0]}",
                buttons=veriler[1],
                link_preview=False,
            )
        else:
            return await event.answer("You are not authorized to use me! \nยฉ ีัเธเธ เนเธฃ-ืงะณเน โข", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"Information\[(\d*)\]\((.*)\)")))
    async def Information(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        page = int(event.data_match.group(1).decode("UTF-8"))
        commands = event.data_match.group(2).decode("UTF-8")
        try:
            buttons = [
                custom.Button.inline("๐ฉ " + cmd[0] + " ๐ช", data=f"commands[{commands}[{page}]]({cmd[0]})")
                for cmd in CMD_HELP_BOT[commands]["commands"].items()
            ]
        except KeyError:
            return await event.answer("No Description is written for this plugin", cache_time=0, alert=True)

        buttons = [buttons[i : i + 2] for i in range(0, len(buttons), 2)]
        buttons.append([custom.Button.inline(f"{rishu_emoji} Main Menu {rishu_emoji}", data=f"page({page})")])
        if event.query.user_id in auth:
            await event.edit(
                f"**๐ File :**  `{commands}`\n**๐ข Number of commands :**  `{len(CMD_HELP_BOT[commands]['commands'])}`",
                buttons=buttons,
                link_preview=False,
            )
        else:
            return await event.answer("You are not authorized to use me! \nยฉ ีัเธเธ เนเธฃ-ืงะณเน โข", cache_time=0, alert=True)


    @tgbot.on(callbackquery.CallbackQuery(data=compile(b"commands\[(.*)\[(\d*)\]\]\((.*)\)")))
    async def commands(event):
        cids = await client_id(event, event.query.user_id)
        ultronceo, rishu_USER, rishu_mention = cids[0], cids[1], cids[2]
        auth = await clients_list()
        cmd = event.data_match.group(1).decode("UTF-8")
        page = int(event.data_match.group(2).decode("UTF-8"))
        commands = event.data_match.group(3).decode("UTF-8")
        result = f"**๐ File :**  `{cmd}`\n"
        if CMD_HELP_BOT[cmd]["info"]["info"] == "":
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โ ๏ธ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
        else:
            if not CMD_HELP_BOT[cmd]["info"]["warning"] == "":
                result += f"**โ ๏ธ Warning :**  {CMD_HELP_BOT[cmd]['info']['warning']}\n"
            result += f"**โน๏ธ Info :**  {CMD_HELP_BOT[cmd]['info']['info']}\n"
        sextraa = CMD_HELP_BOT[cmd]["extra"]
        if sextraa:
            a = sorted(sextraa.keys())
            for b in a:
                c = b
                d = sextraa[c]["content"]
                result += f"**{c} :**  `{d}`\n"
        result += "\n"
        command = CMD_HELP_BOT[cmd]["commands"][commands]
        if command["params"] is None:
            result += f"**๐  Commands :**  `{HANDLER[:1]}{command['command']}`\n"
        else:
            result += f"**๐  Commands :**  `{HANDLER[:1]}{command['command']} {command['params']}`\n"
        if command["example"] is None:
            result += f"**๐ฌ Explanation :**  `{command['usage']}`\n\n"
        else:
            result += f"**๐ฌ Explanation :**  `{command['usage']}`\n"
            result += f"**โจ๏ธ For Example :**  `{HANDLER[:1]}{command['example']}`\n\n"
        if event.query.user_id in auth:
            await event.edit(
                result,
                buttons=[custom.Button.inline(f"{rishu_emoji} Return {rishu_emoji}", data=f"Information[{page}]({cmd})")],
                link_preview=False,
            )
        else:
            return await event.answer("You are not authorized to use me! \nยฉ ีัเธเธ เนเธฃ-ืงะณเน โข", cache_time=0, alert=True)


# THANOSPRO
