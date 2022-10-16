import unittest
import re

from cal import Calendar
from __init__ import *

class GetReplyTests(unittest.TestCase):
    

    def test_get_reply(self):
        teststr = "hi"
        reply = getReply(teststr)
        self.assertTrue(
            reply in [
                "Hello, how are you?",
                "Hi! How can I help?",
                "Well hello there!",
                "Bonjour!",
            ]
        )
        
        reply = getReply("fuck you")
        self.assertTrue(
            reply in [
                "The language you've used is offensive or inappropriate for discussion. Please ask something else.",
                "Please no profanity!",
                "Please do not use words that hurt my ears!",
                "Woah, please be nice to me!"
            ]
        )

        reply = getReply("sad")
        self.assertTrue(
            reply in [
                "Please elaborate!",
                "I do not understand. Can you try again?",
                "I may be a bot, but I can't read your mind!!",
                "What are you trying to say to me?",
                "Please dont speak giberish!"
            ]
        )

        reply = getReply("true")
        self.assertTrue(
            reply in [
                "Please elaborate!",
                "I do not understand. Can you try again?",
                "I may be a bot, but I can't read your mind!!",
                "What are you trying to say to me?",
                "Please dont speak giberish!"
            ]
        )

    def test_google_oauth(self):
        cal = Calendar()
        cal.login()
        cal_list = cal.get_calendar_list()
        events = cal.get_events()

        self.assertTrue(type(events) == list)
        self.assertTrue(type(events[0]) == dict)
        self.assertTrue(type(events[0]["summary"]) == str)


    def test_weather(self):
        teststr = "Perth"
        reply = getReply(f"what's the weather in {teststr}")
        self.assertFalse(
            re.match("The weather in .* at .* is .* at temperature .* °C ", reply) == None
        )

    def test_translate(self):
        teststr = "por que no los dos"
        self.assertTrue(getReply(f"translate {teststr}") == "why not both")

class GetServerTest(unittest.TestCase): 
    def test_server(self):
        '''Tests to see if server is running'''
        testmsg = "Do you like movies?"
        self.assertFalse(get_chatbot_reply(testmsg) == "Couldn't connect to bot")

if __name__=="__main__":
    unittest.main()