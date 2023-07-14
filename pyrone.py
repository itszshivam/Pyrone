import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=23330007, api_hash="59b6d22c9fd9538b0088fb8453234bff")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=23330007, api_hash="59b6d22c9fd9538b0088fb8453234bff")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=23330007, api_hash="59b6d22c9fd9538b0088fb8453234bff")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=23330007, api_hash="59b6d22c9fd9538b0088fb8453234bff")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=23330007, api_hash="59b6d22c9fd9538b0088fb8453234bff")
else:
    M5 = None


ONE_WORDS = ["MADARCHOD", "TUJHE", "PELTA", "HU", "BAAP", "SE", "BHIR", "GYA NA", "AB TERI", "MAA", "CHODTA HU",
             "TERI", "MAA", "KI", "CHUT", "MEIN", "MERA", "LUND", "AUR", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "CHUTIYE", "TERA", "BAAP",
           "HU", "MAI", "BACHE", "SPEED", "PAKAD", "BHEN KE LAUDE", "TERI MAA", "KI CHUT", "MEIN", "KUTTE KI", "TATTI",
           "MAI AB", "TERI ", "MAA", "KO", "KUTTIYA", "KI", "TARAH", "CHODUNGA", "TERI", "MAA", "KE", "BHOSDE",
           "MEIN", "LOUD SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "BHEN", "KO", "AIDS KE", "PATIENT", "SE CHODWAUNGA", "TERI", "BHEN", "KE", "BOOBS",
           "DABAUNGA","MADARCHOD","TERI","MAA","KAA","CHUT","MARUGA","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERE","GAAND","MEIN","BAWASIR","CHUTIYA","RANDI","KEE","PILLE","TERE","LUND",
           "MEIN","NASBANDI","KRWA","DUNGA","BEHENCHOD","TERA","BAAP","APNI","PATNI","KO","MERE PAS","LAYA",
           "THA","CHUDWANE","LAURE","AUR SUN","SHIVAM OP","BOLTE","BETA HAI TU","MERA","MAI SHIVAM","TERA","BAAP HU","RANDI KE",
           "PILLE","GAANDU","TERII","BEHEN","KAAA","BOOBS","MEIN","INJECTION","GHUSERU","LAURE","TERA","APNA","DNA","KRWA",
           "SHIVAM","TERA","BAAP","NIKLEGA","TERA","PURE","KHANDAN", "KO", "CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","TERA","LAURA","KAAT KE","FEK","DUNGA","BAAP", "BOL", "MEREKO", "TERI", "BHEN", "KA", "GAAND", "CHAURA",
           "AUR", "TU", "BETAA","CHUSS","LEEE",
           "MERAA","LOURA","JAISE","ALUU","KAAA","PAKORA","TERI","MAAA","BHEN","GF","MAUSI","","DIN", "RAAT","SOTEE",
           "JAGTEE","AIDS KE","PATIENT","SE CHUDWAYEGI", "AUR", "SUN", "CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LAURE","SMJHA NA","MERA BETA",
           "HAHAHA","BOL","RANDI","AUR", "LAREGA", "KYA", "RANDI KE", "MADARCHOD", "BHEN KE LAURE", 
           "GAAR", "MAAR", "LUNGA", "MAI", "TERI", "BHOSDIKE", "AUR SUN TU", "TERI", "MAA", "KE",
           "BOOBS", "BADE", "BADE", "AUR", "TEREKO","PEL DUNGA", "KHARE", "KHARE", "TERI", "BHEN KE", "CHUT ME",
           "52 GAJ", "KA", "LUND", "TERI","BHEN", "KO", "AISA", "PELUGA", "KI", "GHAR TAK", "BACHA", "DETE",
           "DETE", "JAYEGI", "TU", "MADARCHOD", "RANDI KE", "SPEED", "PAKAR", "MERI", "SAALE", "GAAND", "FATT", "KE", "72 HO GAYI NA",
           "CHUTTAR", "KE","AULAAD", "GAANDU", "BHADWE", "KE", "AULAAD", "TERI", "MAA BHEN", "KE", "NUDES", "BECHUNGA",
           "AUR","TERI MAA","KO","RANDI","BANA","DUNGA","BHAG","JAA","YAHAN","SE","BHOSDIKE","NAHI TOH","TERI","MAIYA","FIR",
           "SE", "CHUDEGI", "SUAR","KEE","CHODE", "TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUR","TERI",
           "MAA","150","MEIN","BIK","JAATI","AUR","TERI","BHEN", "KE", "TIGHT", "CHUT KO",
           "CHOD CHOD", "KAR", "LOOSE", "KAR DUNGA","AUR","TERI","MAA KE","CHUT MEIN","HAATHI","KAA",
           "LUND","DAAL","DUNGA","BEHEN","KE","LAURE","TU","SAALE","KUTTE","KE","CHODE","INSAAAN","TERI","LULLI",
           "KUTTE","SE BHI","CHHOTI","SMJHA NA","MADHARCHOD","BAAP SE","BAKCHODI","NAHI","SHIVAM","TERA BAAP","SPEED","PAKAR",
           "MERI","BHEN KE","LAURE","CHUD","GYA","NA","BETA","APNE BAAP","SE BAKCHODI","KABHI","NAHI","KARTE","SMJHA",
           "NA","BACCHA","AUKAAT ME","RAHO","WARNA","KHANDAN","CHOD","DENGE","TUMHARI"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.3)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["AJJA"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["XD"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["AJJA"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["XD"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["AJJA"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["XD"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["AJJA"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["XD"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["AJJA"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["XD"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("TheAltron")

if M2:
    M2.start()
    M2.join_chat("TheAltron")

if M3:
    M3.start()
    M3.join_chat("TheAltron")

if M4:
    M4.start()
    M4.join_chat("TheAltron")

if M5:
    M5.start()
    M5.join_chat("TheAltron")

print("Pyrone Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
