import interface 
import cal
import pyjokes

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import scraper
import weather
from googletrans import Translator

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
trainer.train(
    "chatterbot.corpus.english"
)

def getReply(msg):
    msg = msg.lower().strip()
    if (msg == "hi"):
        reply = "Hello, how are you?"
    elif (msg == "bye"):
        reply = "Goodbye"
    elif ("search" in msg):
        reply = scraper.google_search(msg.replace("search ", ""))
    elif ("what" in msg and "weather" in msg):
        reply = weather.weather(msg)
    elif (msg.startswith("translate")):
        translator = Translator()
        translation = translator.translate(msg.replace("translate ", ""))
        reply = translation.text
    elif ("what" in msg and "coming up" in msg):
        reply = "Here's what's coming up\n" + "\n".join([e["start"]+" "+e["summary"] for e in account.get_events()])
    elif (msg.startswith("tell me a joke")):
        reply = pyjokes.get_joke(language='en', category='neutral')
    elif(msg):
        reply = chatbot.get_response(msg)
    else:
        reply = "I do not understand"

    return reply

if __name__=="__main__":
    account = cal.Calendar()
    window = interface.create_window(getReply, account)
    window.mainloop()