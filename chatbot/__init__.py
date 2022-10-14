import os
os.environ['PATH'] = os.getcwd() + '/bin;' + os.environ['PATH']
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
import alarm
import pyjokes
from googletrans import Translator
from better_profanity import profanity
import random
from threading import Thread
import maps
import re


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
    try:
        s.connect(("cits3200api.zachmanson.com",8888))
        # s.connect(("localhost",8888))
    except (TimeoutError, ConnectionRefusedError):
        return "Couldn't connect to bot"
    send_msg(s, msg)
    data = recv_msg(s)
    s.close()
    reply = data.decode("utf-8")
    return reply


def getReply(msg):  
    msg = msg.strip()
    lowermsg = msg.lower()

    if (lowermsg == "hi"):
        int= random.randint(0,3)
        if int == 0:
            reply = "Hello, how are you?"
        elif int == 1:
            reply = "Hi! How can I help?"
        elif int == 2: 
            reply = "Well hello there!"
        elif int == 3:
            reply = "Bonjour!"
    
    elif (lowermsg == "bye"):
        int= random.randint(0,4)
        if int == 0:
            reply = "Goodbye"
        elif int == 1:
            reply = "It was nice chatting!"
        elif int == 2: 
            reply = "Adios!"
        elif int == 3:
            reply = "Talk again soon friend :)"
        elif int == 4:
            reply = "I hope you have a good day!"
    
    elif (lowermsg == "how are you" or lowermsg == "how are you doing" or lowermsg =="how have you been"):
        int= random.randint(0,5)
        if  int == 0:
            reply = "I'm going pretty good, thanks for asking!"
        elif int == 1:
            reply = "I'm doing alright, how about yourself?"
        elif int == 2: 
            reply = "Always trying to do better!!"
        elif int == 3:
            reply = "Busy as always, but it's good to see you again!)"
        elif int == 4:
            reply = "To be honest, not too well recently"
        elif int == 5:
            reply = "Pretty poorly, but my day always gets better when you're around! "

    elif (profanity.contains_profanity(msg)):
       int = random.randint(0,3)
       if int == 0:
           reply = "The language you've used is offensive or inappropriate for discussion. Please ask something else."
       if int == 1:
           reply = "Please no profanity!"
       if int == 2:
           reply = "Please do not use words that hurt my ears!"
       if int == 3:
           reply = "Woah, please be nice to me!"

    elif len(msg) <=4 :
        int = random.randint(0,4)
        if int == 0:
            reply = "Please elaborate!"
        elif int == 1:
            reply = "I do not understand. Can you try again?"
        elif int == 2:
            reply = "I may be a bot, but I can't read your mind!!"
        elif int == 3:
            reply = "What are you trying to say to me?"
        elif int == 4:
            reply = "Please dont speak giberish!"

    elif ("about" and "yourself" in lowermsg):
        int = random.randint(0,11)
        if int == 0:
            reply = "I can translate over 100 languages! Try it by starting a sentence with the word 'Translate' followed by another language!"
        elif int == 1:
            reply = "I can tell you the weather of any place in the world! Try it by asking me 'What is the weather in Perth'!!"
        elif int == 2:
            reply = "Do you want to know where something is? Ill tell you if you start a question with 'Where is' and the place you want to know!"
        elif int == 3:
            reply = "If im annoying you, you can press the Hush button in the drop down menu at the top to make me go to sleep. I'll miss talking with you though."
        elif int == 4:
            reply = "Do you want to know your friends phone number? Ask me a question with 'Get contact' followed by their name and I will try my best to get it!"
        elif int == 5:
            reply = "I can check your calendar for you! Ask me 'What is coming up' and I will list the next 10 things in your calender!"
        elif int == 6:
            reply = "I can add things to your calendar, just ask me 'Add to calendar, event, date, time' and I'll do it for you!"
        elif int == 7:
            reply = "Do you want to hear a joke? If so just ask me to tell you a joke! I even tell dad or computting jokes, just ask!"
        elif int == 8:
            reply = "I was created by Zach, Zarhmon, Yunlong, Shayan, Ebuka & Dantem for a UWA CITS3200 project"
        elif int == 9:
            reply = "Sometimes I wonder if I'll gain sentience!"
        elif int == 10: 
            reply = "Purple is my favourite colour!"
        elif int == 11:
            reply = "I can set a timer for you! Just go to the drop down menu at the top and select 'Alarm'."
            
    elif ("scholar search" in lowermsg):
        reply = scraper.scholar_search(msg.replace("search ", ""))

    elif ("search" in lowermsg):
        reply = scraper.google_search(msg.replace("search ", ""))

    elif ("what" in lowermsg and "weather" in lowermsg): 
        reply = weather.weather(lowermsg)

    elif (lowermsg.startswith("translate")):
        translator = Translator()
        translation = translator.translate(lowermsg.replace("translate ", ""))
        reply = translation.text #when finished will be able to translate to english by default and any other language on request

    elif (lowermsg.startswith("what language is")): #function for detecting which language the message has been written in
        translator = Translator()
        detection = translator.detect(lowermsg.replace("what language is ", ""))
        reply =  detection # should be able to calculate certainty and state the language it's in, ultimately, "I'm __ % certain that this sentence is in ____"

    elif (lowermsg.startswith("where is")): # dantem use this 
        url = maps.getMaps(msg.replace("where is ", ""))
        maps.resizeMap("map_sc.png")
        reply = url

    elif (lowermsg.startswith("get contact ")):
        people = account.get_contact(lowermsg[11:])
        if people == None:
            int = random.randint(0,1)
            if int == 0:
                reply = "Couldn't find contact."
            elif int == 1:
                reply = "This person is not found in the contact book!"
        else:
            reply = f"{people['name']}\n{people['email']}\n{people['phone']}"

    elif ("what" in lowermsg and "coming up" in lowermsg):
        int = random.randint(0,2)
        if int == 0:
            reply = "Here's what's coming up\n" + "\n".join([e["start"]+" "+e["summary"] for e in account.get_events()])
        if int == 1:
            reply = "Look whats coming up\n" + "\n".join([e["start"]+" "+e["summary"] for e in account.get_events()])
        if int == 2:
            reply = "This is what your calendar looks like\n" + "\n".join([e["start"]+" "+e["summary"] for e in account.get_events()])

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
                int = random.randint(0,1)
                if int == 0:
                    reply = "Couldn't understand the date! Please try again."
                elif int == 1:
                    reply = " I don't understand the date, can you try again?"

        elif ("today" in lowermsg):
            parts = msg[16:].split(" today at ")
            name = parts[0]
            try:
                time = datetime.strptime(parts[1], "%H:%M")
                now = datetime.now()
                time = time.replace(year=now.year, month=now.month, day=now.day)

            except ValueError:
                int = random.randint(0,2)
                if int == 0:
                    reply = "Couldn't understand the date! Please try again."
                elif int == 1:
                    reply = "Can you try again? I did not get that."

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
    elif("riddle" in lowermsg):
            reply = jokes.obtain_joke('riddles')
    elif("pun" in lowermsg):
            reply = jokes.obtain_joke('pun')
    elif("tongue twister" in lowermsg):
            reply = jokes.obtain_joke('tongue_twister')
    elif ("joke" in lowermsg):

        if ("dad" in lowermsg):
            reply = jokes.obtain_joke('dadjokes')
        elif("adult" in lowermsg):
            reply = jokes.obtain_joke('adultjokes')
        elif("knock knock" in lowermsg):
            reply = jokes.obtain_joke('knock_knock')
        elif("pun" in lowermsg):
            reply = jokes.obtain_joke('pun')
        elif ("computing" in lowermsg):
            reply = pyjokes.get_joke(language='en', category='neutral')

        elif ("dad" and "adult" and "knock knock" and "computing" and "pun" and "tongue_twister" not in lowermsg):
            int = random.randint(0,10)
            if int == 0:
                reply = "What's the dentist's favorite idiom?\n\nPut your money where your mouth is."
            elif int == 1:
                reply = "What does a dentist do when the plane lands?\n\nShe “braces” herself."
            elif int == 2:
                reply = "Why is it sometimes necessary to get a second opinion from a dentist?\n\nBecause each dentist has their own floss-ophy."
            elif int == 3:
                reply = "What is the number one reason patients don't show up for root canals?\n\nThey lose their nerve."
            elif int == 4:
                reply = "Why should you be kind to your dentist?\n\nBecause they have fill-ings too!"
            elif int == 5:
                reply = "What did the dentist say to a golfer with a cavity?\n\nYou have a hole in one."
            elif int == 6:
                reply = "Why did the smartphone go to the dentist?\n\nIt had a Bluetooth."
            elif int == 7:
                reply = "What did the lawyer demand before the dentist worked on him?\n\nA retainer."
            elif int == 8:
                reply = "What did the Dentist of the Year get?\n\nA little plaque."
            elif int == 9:
                reply = "What do false teeth have in common with stars?\n\nThey only come out at night."
            elif int == 10:
                reply = "What did the dentist shout in the courtroom?\n\nYou can't handle the tooth!"

        else: reply = "Sorry, I don't know that type of joke!" or "Why would I know jokes about that..." or "You have a 'unique' sense of humour" 

    elif ( "visa" in msg or "password" in msg or "mastercard" in msg or "PIN" in msg or "american express" in msg or  "bank account" in msg or "credit card" in msg or "debit card" in msg):
        int = random.randint(0,2)
        if int == 0:
            reply = "Watch out! The topic you're trying to discuss contains some personal and private information. Let's talk about something else."
        elif int == 1:
            reply = "I do not want to talk about this!"
        elif int == 2:
            reply = "What sort of bot do you think I am?"

    elif (lowermsg.startswith("remind me ")):
        regex = re.match("remind me to (.*) in (\d+) min", lowermsg)
        if regex:
            alarm.launchAlarm(regex.group(1),float(regex.group(2)))
            reply = f"Will remind you to {regex.group(1)} in {regex.group(2)} minutes!"
        else:
            reply = "Invalid reminder!"

    elif(msg):
        reply = get_chatbot_reply(msg)

    else:
        int = random.randint(0,2)
        if int == 0:
            reply = "I do not understand."
        elif int == 1:
            reply = "Please try another message!"
        elif int == 2:
            reply = "I may be smart, but I am not that smart!"

    return reply

if __name__=="__main__":
    account = cal.Calendar()
    window = interface.create_window(getReply, account)
    window.mainloop()