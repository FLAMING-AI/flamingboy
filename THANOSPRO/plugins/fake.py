import asyncio
import os
import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins

from . import *

@rishu_cmd(pattern="fpic$")
async def _(event):
    cid = await client_id(event)
    rishu_mention = cid[2]
    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    rishu = await eor(event, "`Creating a fake face...`")
    if response.status_code == 200:
      with open("THANOSPRO.jpg", 'wb') as f:
        f.write(response.content)
    else:
        return await eod(rishu, "Failed to create Fake Face! Try again later.")
    captin = f"Fake Image By {rishu_mention}"
    fole = "THANOSPRO.jpg"
    await event.client.send_file(event.chat_id, fole, caption=captin, force_document=False)
    await rishu.delete()
    os.system("rm /root/THANOSPRO/THANOSPRO.jpg ")


@rishu_cmd(pattern="fake ([\s\S]*)")
async def _(event):
    await event.delete()
    input_str = event.pattern_match.group(1)
    action = "typing"
    if input_str:
        action = input_str
    async with event.client.action(event.chat_id, action):
        await asyncio.sleep(86400)


@rishu_cmd(pattern="gbam$")
async def gbun(event):
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "`Warning!! User ππ½πΌππππΏ By Admin...\n`"
    no_reason = "**Reason:**  __Madarchod Saala__"
    rishu = await eor(event, "** Nikal LawdeβοΈβοΈβ οΈ**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in event.client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.sender_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.sender_id
        if idd == 2132012729:
            await rishu.edit("`Wait a second, This is my master!`\n**How dare you threaten to ban my master nigger!**\n\n__Your account has been hacked! Pay 69$ to my master__ [rishabh](https://t.me/ultronceo) __to release your account__π", link_preview=False)
        else:
            jnl = (
                "`Warning!! `"
                "[{}](tg://user?id={})"
                "` ππ½πΌππππΏ By Admin...\n\n`"
                "**Person's Name: ** __{}__\n"
                "**ID : ** `{}`\n"
            ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Victim Nigga's username: ** `Doesn't own a username!`\n"
            elif usname != "None":
                jnl += "**Victim Nigga's username** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **" + gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await rishu.edit(jnl)
    else:
        mention = "`Warning!! User ππ½πΌππππΏ By Admin...\nReason: Not Given `"
        await rishu.edit(mention)


CmdHelp("fake").add_command(
  'fake', '<action>', 'This shows the fake action in the group  the actions are typing, contact, game ,location, voice, round, video, photo, document.'
).add_command(
  'gbam', '<reason> (optional)', 'Fake gban. Just for funπ€'
).add_command(
  'picgen', None, 'Gives a fake face image'
).add_info(
  'Fake Actions.'
).add_warning(
  'β Harmless Module.'
).add()
