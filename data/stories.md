#story 0
* greet
   - utter_greet
* goodbye
   - utter_goodbye

# story 1
* greet
   - utter_greet
* ask_about_sell4bids
   - utter_sell4bids
* goodbye
   - utter_goodbye
   
# story 2
* greet
   - utter_greet
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* goodbye
   - utter_goodbye
   
# story 2
* greet
   - utter_greet
* ask_about_sell4bids
   - utter_sell4bids
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* goodbye
   - utter_goodbye
   
# story 3
* greet
   - utter_greet
* ask_about_sell4bids
   - utter_sell4bids
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* goodbye
   - utter_goodbye
   
# story 4
* greet
   - utter_greet
* ask_howto
   - utter_howto
* goodbye
   - utter_goodbye

# story 5
* greet
   - utter_greet
* ask_howto
   - utter_howto
* ask_listening_posting_on_socialmedia
   - utter_listening_posting_on_socialmedia
* goodbye
   - utter_goodbye