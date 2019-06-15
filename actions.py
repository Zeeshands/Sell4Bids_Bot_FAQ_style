from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
import random

class ActionFAQ(Action):

    def name(self):
        return "action_faq"

    def run(self, dispatcher, tracker, domain):
           #get the original intent from tracker.latest_message and retrieve the correct answer
           full = tracker.latest_message.__str__()
           intent = tracker.latest_message['intent'].get('name')

           if intent == 'faq.greet':
               #tup1 = ("Hello! How can I help" , "Good day & how may I help you!")
               #res = tup1[random.randint(0, 2)]
               res = 'Hello! How can I help'
           elif intent == 'faq.banner':
               res = 'Hi, I am Sell4Bids ChatBot, How can I help you'

           elif intent == 'faq.goodbye':
               res = 'Bye Bye'
               #tup1 = ("Bye bye: (" , "Take care !")
               #res = tup1[random.randint(0, 2)]

           elif intent == 'faq.ask_products':
               res = 'On Sell4Bids, you can buy and sell almost anything: new and used products, handmade items and crafts, gift cards'

           elif intent == 'faq.ask_about_sell4bids':
                res = 'It is the auction universe. Fast, easy,cool. It provedes the next generation AI platform to connect sellers,services,stuff &jobs with buyers.'

           elif intent == 'faq.ask_howto':
               entity = (tracker.latest_message['entities'][0]).get('value').__str__()
               if entity in ('sellers','auctioneers'):
                res = 'You signup ,setup your sellers profile, Take photo Auction,jobs, Chat with buyers, Turn stuff into cash'
               elif entity in ('buyers', 'bidders'):
                res = 'You signup, search or browse stuff, bid or buy, buy in person, leverage our AI, shop with a roar'

           elif intent == 'faq.ask_howto_post':
               res = 'Create an account and tap the “Sell or Auction Now”. \
                      Select the desired listing category among Vehicles, Services, Jobs and Other Items.\
                      Then fill the required fields and list it for Sale or Auction.'

           elif intent == 'faq.ask_listening_posting_on_socialmedia':
               res = 'Yes, you can share your listing to other applications. After successfully listing the item, you can share your listing from item detail page.'

           elif intent == 'faq.ask_what_to_buysell':
               res = 'On Sell4Bids, you can buy and sell almost anything: new and used products, handmade items and crafts, gift cards'

           elif intent == 'faq.ask_if_listening_sold':
               res = 'When you''ve sold a listing, mark it as sold to let other users know it''s no longer available!'

           elif intent == 'faq.ask_where_listening_posted':
               res = 'If you want to see all the listings you''ve posted, go to MySell4Bids and tap on Selling tab. Here you can also see the Watch-listed, Sold, Auctioned listings.'

           elif intent == 'faq.ask_listening_payment':
               res = 'No, Currently you don’t have to pay for listing on Sell4Bids. You can list as many items as you want to sell.'

           dispatcher.utter_message(res)
