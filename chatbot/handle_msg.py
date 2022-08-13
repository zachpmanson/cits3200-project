from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

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
    if (msg == "Hi"):
        reply = "Hello, how are you?"
    elif (msg == "Bye"):
        reply =  "Goodbye"
    elif(msg):
        reply = chatbot.get_response(msg)
    else:
        reply = "I do not understand"

    return reply