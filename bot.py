from telethon.sync import TelegramClient
from telethon import *
from telethon.errors import SessionPasswordNeededError
import configparser
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
from telethon import Button
from telethon.sync import custom
import logging
import requests
import re
from sys import argv
from prettytable import PrettyTable
chat = 1436992328
api_id = 7215939
api_hash = 'd32de69a9742527f16088a0b8b474c4f'
phone = +919341564618
username = 'r0ld3x'
def pregs(dets):
    arrays = re.findall(r'[0-9]+', dets)
    return arrays
from telethon import TelegramClient
from telethon.sync import TelegramClient
client = TelegramClient(username, api_id, api_hash)
client.start()    

with client:
          while True:
            chat = client.get_entity('MoroccanBinners_csc')
            chatidbmro  = 1345686737
            file1 = open("myfile.txt")  
            ofid = file1.read()
            ofid = int(ofid)
            file1.close()  
            message = client.iter_messages(chat,reverse=True,offset_id=ofid) #
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("myfile.txt", 'w')  
             file.write(str(m))
             file.close()  
             list = pregs(title)
             bin = list[8]
             cc = list[0]
             if len(cc) != 16:
              break
             country = requests.get("https://unimpeachable-faste.000webhostapp.com/con.php?lista=" + bin).text
             if len(country) == 0:
              country = 'N.A'
             bank = requests.get("https://unimpeachable-faste.000webhostapp.com/bank.php?lista=" + bin).text
             if len(bank) == 0:
              country = 'N.A'
             mes = list[1]
             ano = list[2]
             cvv = list[3]
             lista = list[0] + "|" + list[1] + "|" + list[2] + "|" + list[3]
             respo = "<b>╔══════════════════════\n╟ • ROLDEXVERSE/SCRAPPER\n╠ » CC: " + cc +"\n╟    ╙ EXP: "+mes+"| "+ano+" \n╟       ╙ CVV: "+cvv+"\n╟ » CHK: <code>"+lista+"</code>\n╠ » BIN: [" + bin + "]->[" + bank +"[" + country + "]\n╠ » CHANNEL: <code>@RoldexVerse</code>\n╠ » GROUP: <code>@RoldexVerseChats</code>\n╠ » Owner: <code>@r0ld3x</code>\n╚══════════════════════</b>"
             client.send_message('roldexverse', respo,parse_mode='html'            )
            chat = client.get_entity('BinsGram')
            file1 = open("my.txt")  
            ofid = file1.read()
            ofid = int(ofid)
            file1.close()  
            message = client.iter_messages(chat,reverse=True,offset_id=ofid) #
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("my.txt", 'w')  
             file.write(str(m))
             file.close()  
             list = pregs(title)
             cc = list[0]
             if len(cc) != 16:
              break
             country = requests.get("https://unimpeachable-faste.000webhostapp.com/con.php?lista=" + bin).text
             if len(country) == 0:
              country = 'N.A'
             bank = requests.get("https://unimpeachable-faste.000webhostapp.com/bank.php?lista=" + bin).text
             if len(bank) == 0:
              country = 'N.A'
             mes = list[1]
             ano = list[2]
             cvv = list[3]
             lista = list[0] + "|" + list[1] + "|" + list[2] + "|" + list[3]
             respo = "<b>╔══════════════════════\n╟ • ROLDEXVERSE/SCRAPPER\n╠ » CC: " + cc +"\n╟    ╙ EXP: "+mes+"| "+ano+" \n╟       ╙ CVV: "+cvv+"\n╟ » CHK: <code>"+lista+"</code>\n╠ » BIN: [" + bin + "]->[" + bank +"[" + country + "]\n╠ » CHANNEL: <code>@RoldexVerse</code>\n╠ » GROUP: <code>@RoldexVerseChats</code>\n╠ » Owner: <code>@r0ld3x</code>\n╚══════════════════════</b>"
             client.send_message('roldexverse', respo,parse_mode='html'            )
            chat = client.get_entity('https://t.me/joinchat/y8-dee-PXxI5MDll')
            file1 = open("myf.txt")  
            ofid = file1.read()
            ofid = int(ofid)
            file1.close()  
            message = client.iter_messages(chat,reverse=True,offset_id=ofid) #
            for msg in message:
             message = msg
             title = msg.text
             m = msg.id
             file = open("myf.txt", 'w')  
             file.write(str(m))
             file.close()  
             list = pregs(title)
             cc = list[0]
             if len(cc) != 16:
              break
             country = requests.get("https://unimpeachable-faste.000webhostapp.com/con.php?lista=" + bin).text
             if len(country) == 0:
              country = 'N.A'
             bank = requests.get("https://unimpeachable-faste.000webhostapp.com/bank.php?lista=" + bin).text
             if len(bank) == 0:
              country = 'N.A'
             mes = list[1]
             ano = list[2]
             cvv = list[3]
             lista = list[0] + "|" + list[1] + "|" + list[2] + "|" + list[3]
             respo = "<b>╔══════════════════════\n╟ • ROLDEXVERSE/SCRAPPER\n╠ » CC: " + cc +"\n╟    ╙ EXP: "+mes+"| "+ano+" \n╟       ╙ CVV: "+cvv+"\n╟ » CHK: <code>"+lista+"</code>\n╠ » BIN: [" + bin + "]->[" + bank +"[" + country + "]\n╠ » CHANNEL: <code>@RoldexVerse</code>\n╠ » GROUP: <code>@RoldexVerseChats</code>\n╠ » Owner: <code>@r0ld3x</code>\n╚══════════════════════</b>"
             client.send_message('roldexverse', respo,parse_mode='html'            )

        
        
        
