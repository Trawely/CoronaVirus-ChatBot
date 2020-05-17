## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## custom path
* greet
  - utter_greet
* mood_great
  - utter_happy
* uc_ask_name
  - utter_acknowledge
  - utter_disclaimer
* uc_about_covid
  - action_about_covid
* uc_state_by_covid
  - action_state_by_covid
  - action_reset_slot
  - utter_did_that_help
* uc_covid_news
  - action_covid_news
  - utter_did_that_help
* uc_covid_precautions
  - utter_covid_precautions
  - utter_did_that_help
* affirm
  - utter_provide_feedback
* uc_feedback
  - utter_thankyou_feedback

## fallbackpolicy
* uc_chitchat
  - utter_default


## interactive_story_1
* greet
    - utter_greet
* mood_great
    - utter_happy
* uc_ask_name{"name": "Atul"}
    - slot{"name": "Atul"}
    - utter_acknowledge
    - utter_disclaimer
* uc_state_by_covid
    - action_state_by_covid
    - action_reset_slot
    - reset_slots
    - utter_did_that_help
* uc_feedback
    - utter_thankyou_feedback

## developed story
* uc_developed_by
  - utter_developed_by