from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionTellProducts(Action):
    def name(self):
        return 'action_howto'

    def run(self, dispatcher, tracker, domain):
        bs = str(tracker.get_slot('buyerseller'))
        if (bs=='sellers' or bs=='auctioneers'):
         response = "You signup\nsetup your sellers profile\nTake photo Auction,jobs\nChat with buyers\nTurn stuff into cash"
        if (bs=='buyers' or bs=='bidders'):
         response = "You signup\nsearch or browse stuff\nbid or buy\nbuy in person\nleverage our AI\nshop with a roar"

        dispatcher.utter_message(response)
