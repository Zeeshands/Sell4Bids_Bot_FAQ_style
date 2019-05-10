from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionInformPhonePrice(Action):
    def name(self):
        return 'action_inform_phone_price'

    def run(self, dispatcher, tracker, domain):
        pm = str(tracker.get_slot('phone_model'))
        if pm=='iphone6':
         price=320
        else:
         price=420
        response = """The price for {} is {} dollars.""".format(pm,price)
        dispatcher.utter_message(response)
        return [SlotSet('phone_model', pm)]

#second class

class ActionTellProducts(Action):
    def name(self):
        return 'action_tell_products'

    def run(self, dispatcher, tracker, domain):
        response = "Our products are cell phones."
        dispatcher.utter_message(response)
