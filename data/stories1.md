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
   
# story 6
* greet
   - utter_greet
* ask_what_to_buysell
   - utter_what_to_buysell
* goodbye
   - utter_goodbye
   
# story 7
* greet
   - utter_greet
* ask_if_listening_sold
   - utter_if_listening_sold
* goodbye
   - utter_goodbye
 
# story 8
* greet
   - utter_greet
* ask_where_listening_posted
   - utter_where_listening_posted
* goodbye
   - utter_goodbye
   
# story 9
* greet
   - utter_greet
* ask_listening_payment
   - utter_listening_payment
* goodbye
   - utter_goodbye
   
# story 10
* greet
   - utter_greet
* ask_about_sell4bids
   - utter_sell4bids
* ask_howto
   - utter_howto
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
* ask_listening_posting_on_socialmedia
   - utter_listening_posting_on_socialmedia
* ask_what_to_buysell
   - utter_what_to_buysell
* ask_if_listening_sold
   - utter_if_listening_sold
* ask_where_listening_posted
   - utter_where_listening_posted
* ask_listening_payment
   - utter_listening_payment
* ask_listening_payment
   - utter_listening_payment
* goodbye
   - utter_goodbye

#banner
* banner
   - utter_banner
   
## loose stories
* ask_about_sell4bids
   - utter_sell4bids
   
* ask_howto
   - utter_howto
   
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
   
* ask_howto{"buyerseller":"buyers"}
   - slot{"buyerseller":"buyers"}
   - action_howto
   
* ask_listening_posting_on_socialmedia
   - utter_listening_posting_on_socialmedia
   
* ask_what_to_buysell
   - utter_what_to_buysell
   
* ask_if_listening_sold
   - utter_if_listening_sold
   
* ask_where_listening_posted
   - utter_where_listening_posted
   
* ask_listening_payment
   - utter_listening_payment
   
* ask_listening_payment
   - utter_listening_payment
