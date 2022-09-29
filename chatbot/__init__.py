import asyncio
from datetime import datetime, timedelta
import time
import interface 
import cal
import jokes
import struct
import scraper
import weather
import socket
from googletrans import Translator
from better_profanity import profanity

# Sends packed big endian message 
def send_msg(sock, msg):
    if type(msg) == bytes:
        packed_msg = struct.pack('>I', len(msg)) + msg
    else:
        packed_msg = struct.pack('>I', len(msg)) + msg.encode()
    sock.send(packed_msg)

# Receives a packed bid endian message from a socket
def recv_msg(sock):
    packed_msg_len = force_recv_all(sock, 4)
    if not packed_msg_len:
        return None
    msg_len = struct.unpack('>I', packed_msg_len)[0]
    recved_data = force_recv_all(sock, msg_len)
    return recved_data

# Ensures that all the bytes we want to read on receival are read
def force_recv_all(sock, msg_len):
    all_data = bytearray()
    while len(all_data) < msg_len:
        packet = sock.recv(msg_len - len(all_data))
        if not packet:
            return None
        all_data.extend(packet)
    return all_data

def get_chatbot_reply(msg):
    s = socket.socket()
    s.connect(("cits3200api.zachmanson.com",8888))
    send_msg(s, msg)
    data = recv_msg(s)
    reply = data.decode("utf-8")
    return reply


def getReply(msg):
    msg = msg.strip()
    lowermsg = msg.lower()
    if (lowermsg == "hi"):
        reply = "Hello, how are you?"
    elif (lowermsg == "bye"):
        reply = "Goodbye"
    elif (profanity.contains_profanity(msg)):
        reply = "The language you've used is offesnive or inappropriate for discussion. Please ask something else."
    elif len(msg) <=4 :
        reply = "Please elaborate!"
    elif ("search" in lowermsg):
        reply = scraper.google_search(msg.replace("search ", ""))
    elif ("what" in lowermsg and "weather" in lowermsg):
        reply = weather.weather(lowermsg)
    elif (lowermsg.startswith("translate")):
        translator = Translator()
        translation = translator.translate(lowermsg.replace("translate ", ""))
        reply = translation.text
    elif (lowermsg.startswith("where is")): # dantem use this 
        reply = "The closest result is here: "
    elif (lowermsg.startswith("get contact ")):
        people = account.get_contact(lowermsg[11:])
        if people == None:
            reply = "Couldn't find contact"
        else:
            reply = f"{people['name']}\n{people['email']}\n{people['phone']}"
    elif ("what" in lowermsg and "coming up" in lowermsg):
        reply = "Here's what's coming up\n" + "\n".join([e["start"]+" "+e["summary"] for e in account.get_events()])
    elif (lowermsg.startswith("add to calendar")):
        # add to calendar meeting with yulia today at 16:00 
        # add to calendar meeting with yulia on Sep 20 at 16:00
        time = None
        if (" on " in lowermsg):
            parts = msg[16:].split(" on ")
            name = parts[0]
            try:
                time = datetime.strptime(parts[1], "%b %d at %H:%M")
                time = time.replace(year=datetime.now().year) # defaults to current year
                if time < datetime.now():
                    time = time.replace(year=datetime.now().year+1) # if already occured, add to next year
                
            except ValueError:
                reply = "Couldn't understand the date! Please try again"
        elif ("today" in lowermsg):
            parts = msg[16:].split(" today at ")
            name = parts[0]
            try:
                time = datetime.strptime(parts[1], "%H:%M")
                now = datetime.now()
                time = time.replace(year=now.year, month=now.month, day=now.day)
            except ValueError:
                reply = "Couldn't understand the date! Please try again"
        elif ("tomorrow" in lowermsg):
            parts = msg[16:].split(" tomorrow at ")
            name = parts[0]
            try:
                time = datetime.strptime(parts[1], "%H:%M")
                now = datetime.now()
                time = time.replace(year=now.year, month=now.month, day=now.day)
                time = time + timedelta(days=1)
            except ValueError:
                reply = "Couldn't understand the date! Please try again"

        if (time != None):
            account.create_event(
                title=name,
                desc="",
                start=time.isoformat(),
                end=(time+timedelta(hours=1)).isoformat()
            )
            reply = f"Added '{name}' to calendar on {time.isoformat()}"
    elif ("joke" in lowermsg ):
        if ("dad" in lowermsg):
            reply = jokes.obtain_joke('dadjokes')
        else: reply = "" 
    elif (lowermsg.startswith("tell me a computing joke")):
        reply = pyjokes.get_joke(language='en', category='neutral')
    elif ( "visa" in msg or "password" in msg or "mastercard" in msg or "PIN" in msg or "american express" in msg or  "bank account" in msg or "credit card" in msg or "debit card" in msg):
        reply = "Watch out! The topic you're trying to discuss contains some personal and private information. Let's talk about something else."
    elif(msg):
        reply = get_chatbot_reply(msg)
    else:
        reply = "I do not understand"

    return reply


if __name__=="__main__":
    account = cal.Calendar()
    window = interface.create_window(getReply, account)
    window.mainloop()