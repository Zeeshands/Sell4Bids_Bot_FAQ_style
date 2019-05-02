## story_001
* greet
   - utter_greet
* phone_price{"phone_model":"iphone6"}
   - slot{"phone_model": "iphone6"}
   - action_inform_phone_price
* goodbye
   - utter_goodbye
   - export
   
## Iphone purchase story 1
* greet
   - utter_greet
* phone_price
   - utter_ask_phonemodel
* phone_price{"phone_model":"iphone6"}
   - slot{"phone_model":"iphone6"}
   - action_inform_phone_price
* goodbye
   - utter_goodbye
   - export
   
#story 2
* greet
   - utter_greet
* ask_products
   - action_tell_products
* goodbye
  - utter_goodbye


