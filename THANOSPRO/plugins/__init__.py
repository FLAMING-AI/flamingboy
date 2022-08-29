import datetime
import time

from THANOSPRO import *
from THANOSPRO.clients import *
from THANOSPRO.config import Config
from THANOSPRO.helpers import *
from THANOSPRO.utils import *
from THANOSPRO.random_strings import *
from THANOSPRO.version import __rishu__
from THANOSPRO.sql.gvar_sql import gvarstat
from telethon import version

rishu_logo = "./THANOSPRO/resources/pics/THANOSPRO_logo.jpg"
cjb = "./THANOSPRO/resources/pics/cjb.jpg"
restlo = "./THANOSPRO/resources/pics/rest.jpeg"
shuru = "./THANOSPRO/resources/pics/shuru.jpg"
shhh = "./THANOSPRO/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
rishu_ver = __rishu__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

is_sudo = "True" if gvarstat("SUDO_USERS") else "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "thanospros"
my_group = Config.MY_GROUP or "THANOSPRO_Chat"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/thanospros"
rishu_channel = f"[Շђคภ๏ร-קг๏]({chnl_link})"
grp_link = "https://t.me/THANOSPRO_Chat"
rishu_grp = f"[Շђคภ๏ร-קг๏ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# THANOSPRO
