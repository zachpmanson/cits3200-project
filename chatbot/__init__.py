import asyncio
from datetime import datetime, timedelta
import time
import interface 
import cal
import pyjokes
import jokes

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import scraper
import weather
from googletrans import Translator
from better_profanity import profanity


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
        elif("adult" in lowermsg):
            reply = jokes.obtain_joke('adultjokes')
        elif("knock knock" in lowermsg):
            reply = jokes.obtain_joke('knock_knock')
        else: reply = "" 
    elif (lowermsg.startswith("tell me a computing joke")):
        reply = pyjokes.get_joke(language='en', category='neutral')
    elif ("riddle" in lowermsg):
        reply = jokes.obtain_joke('riddle')
    elif ( "visa" in msg or "password" in msg or "mastercard" in msg or "PIN" in msg or "american express" in msg or  "bank account" in msg or "credit card" in msg or "debit card" in msg):
        reply = "Watch out! The topic you're trying to discuss contains some personal and private information. Let's talk about something else."
    elif(msg):
        reply = chatbot.get_response(msg)
    else:
        reply = "I do not understand"

    return reply


if __name__=="__main__":
    chatbot = ChatBot("Bot1")
    conversation = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]

    trainer = ListTrainer(chatbot)
    trainer.train(conversation)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")
    account = cal.Calendar()
    window = interface.create_window(getReply, account)
    window.mainloop()