from telethon.sync import TelegramClient
from telethon import *
import time
from telethon import events, Button
from telethon import functions, types, events, utils
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.errors import SessionPasswordNeededError
from telethon.tl.types import ReplyInlineMarkup
from telethon.tl.types import KeyboardButtonRow
from telethon.tl.types import KeyboardButtonUrl
import configparser

from telethon import TelegramClient, Button, events 
import json
import asyncio
from datetime import date, datetime
import re
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (
    PeerChannel
)
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from pathlib import Path
import asyncio
from telethon import Button
import logging
import requests
import re
import telethon
from sys import argv
from prettytable import PrettyTable
chat = 1436992328
api_id = 1667849
api_hash = 'b719710209932bff18219f4064e92388'
# api_id = 7239207
#api_hash = 'ed44780dedd182084f2133b16944cf34'
username = 'r0ld3x'
#bot_token = '1795181134:AAH0WHUhuJeGNgK-KJC_aJl4T4WtmPojewY'
    
def pregs(dets):
    arrays = re.findall(r'[0-9]+', dets)
    return arrays
from telethon import TelegramClient
from telethon.sync import TelegramClient
client = TelegramClient(username, api_id, api_hash)
client.start()
# client.add_bot(bot_token)    

with client:
          print("STARTED")
          while True:
           try:
            asyncio.sleep(2)
            file1 = open("Freakdrop.txt", "r+")    
# absolute file positioning 
            file1.seek(0)  
            ofid = file1.read()
            ofid = int(ofid)
            file1.close()  
            message = client.iter_messages('Freakdrop',reverse=True,offset_id=ofid,min_id=ofid,wait_time=3)
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("Freakdrop.txt", 'r+')  
             file.truncate()
             file.write(str(m))
             file.close()  
             list = pregs(title)
             cc = list[0]
             if len(cc) == 0:
              break
             if len(cc) != 16:
              break
             con = requests.get("https://roldex.codes/bank.php?lista=" + cc).text
             if len(con) == 0:
              con = 'N.A'             
             mes = list[1]
             ano = list[2]
             ano1 = list[2]
             cvv = list[3]
             if len(mes) >= 3:
              ano = cvv
              cvv = mes
              mes = ano1
             lista = cc + "|" + mes + "|" + ano + "|" + cvv
             print(lista)
             respo = "<b>•> ROLDEXVERSE CC SCRAPPER\n°> CARD -> <code>" + lista + "</code>\n•> BIN -> " + con +"\n•> CHANNEL -> @RoldexVerse\n•> RECHECK -> @RoldexVerseChats\n•> OWNER -> <code>@r0ld3x</code></b>"
             # 
             file1 = open("ccs.txt", "a")
             m = lista + "\n"
             file1.write(m)
             file1.close() 
             client.send_message('roldexversedrops', respo,parse_mode='html')
             file1 = open("TeamCrditCard.txt", "r+")    
             file1.seek(0)  
             ofid = file1.read()
             ofid = int(ofid)
             file1.close()  
            message = client.iter_messages('TeamCrditCard',reverse=True,offset_id=ofid,min_id=ofid,wait_time=3)
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("TeamCrditCard.txt", 'r+')  
             file.truncate()
             file.write(str(m))
             file.close()  
             list = pregs(title)
             cc = list[0]
             if len(cc) == 0:
              break
             if len(cc) != 16:
              break
             con = requests.get("https://roldex.codes/bank.php?lista=" + cc).text
             if len(con) == 0:
              con = 'N.A'             
             mes = list[1]
             ano = list[2]
             ano1 = list[2]
             cvv = list[3]
             if len(mes) >= 3:
              ano = cvv
              cvv = mes
              mes = ano1
             lista = cc + "|" + mes + "|" + ano + "|" + cvv
             print(lista)
             respo = "<b>•> ROLDEXVERSE CC SCRAPPER\n°> CARD -> <code>" + lista + "</code>\n•> BIN -> " + con +"\n•> CHANNEL -> @RoldexVerse\n•> RECHECK -> @RoldexVerseChats\n•> OWNER -> <code>@r0ld3x</code></b>"
             # 
             file1 = open("ccs.txt", "a")
             m = lista + "\n"
             file1.write(m)
             file1.close() 
             client.send_message('roldexversedrops', respo,parse_mode='html')
             client.send_message('flipzcc', respo,parse_mode='html')
           except errors.FloodWaitError as e:
               print('Have to sleep', e.seconds, 'seconds')
               time.sleep(e.seconds)
