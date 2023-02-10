import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5393510627:AAEJtc-F7py8DbkgNEmM7nMQA7glLuQ3_1w")

API_ID = int(os.environ.get("API_ID", "12679441"))

API_HASH = os.environ.get("API_HASH", "d47d2e2cdb8e048108a44e40494bf1f0")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
