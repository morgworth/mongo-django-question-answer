import pickle
from chatbot import Chatbot

"""
The chatbot model was taken from this article:
https://medium.com/cindicator/building-chatbot-weekend-of-a-data-scientist-8388d99db093
"""
class ChatbotServices(object):

    @staticmethod
    def respond(text):
        bot = Chatbot.ChatBot()
        return bot.reply(text)
