# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import SlotSet
from newsapi import NewsApiClient
from datetime import date,datetime,timedelta
import pandas as pd
import numpy as np
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionAboutCovid(Action):

    def name(self) -> Text:
        return "action_about_covid"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        message_1 = "COVID-19 is the disease caused by the new coronavirus that emerged in China in December 2019."
        message_2 = "COVID-19 symptoms include cough, fever, shortness of breath, muscle aches, sore throat, unexplained loss of taste or smell, diarrhea and headache. COVID-19 can be severe, and some cases have caused death.!"
        message_3 = "The new coronavirus can be spread from person to person. It is diagnosed with a laboratory test."
        message_4 = "There is no coronavirus vaccine yet. Prevention involves frequent hand-washing, coughing into the bend of your elbow, staying home when you are sick and wearing a cloth face covering if you can't practice social distancing."

        dispatcher.utter_message(text=message_1 + "\n")
        dispatcher.utter_message(text=message_2 + "\n")
        dispatcher.utter_message(text=message_3 + "\n")
        dispatcher.utter_message(text=message_4 + "\n")

        return []

class ActionStateByCovid(Action):

    def name(self) -> Text:
        return "action_state_by_covid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        response_we_need = requests.get("https://api.covid19india.org/data.json").json()
        state_slot = tracker.get_slot("e_state_we_need")
        if state_slot == None:
            state = "Total"
            for data in response_we_need["statewise"]:
                if data["state"] == state:
                    print(data)
                    active_cases = data["active"]
                    confirmed_cases = data["confirmed"]
                    deaths = data["deaths"]
                    last_updated = data["lastupdatedtime"]
                    recovered_cases = data["recovered"]
                    message = 'The Total Confirmed Cases in India is around {} from which these are {} total Active Cases!,Total Recovered Cases around {} and Total Deaths around {}.'.format(confirmed_cases,active_cases,recovered_cases,deaths)
        else:
           for data in response_we_need["statewise"]:
                if data["state"] == state_slot.title():
                    print(data)
                    active_cases = data["active"]
                    confirmed_cases = data["confirmed"]
                    deaths = data["deaths"]
                    last_updated = data["lastupdatedtime"]
                    recovered_cases = data["recovered"]
                    message = 'The {} has Confirmed Cases around {} from which these are {} total Active Cases!,Total Recovered Cases around {} and Total Deaths around {}.'.format(state_slot,confirmed_cases,active_cases,recovered_cases,deaths)
        
        dispatcher.utter_message(text = message)
        dispatcher.utter_message('The information was last updated on {}'.format(last_updated))

        return []
    
class ActionResetSlots(Action):

     def name(self) -> Text:
            return "action_reset_slot"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message("Try asking for a New State now!!")

         return [AllSlotsReset()]
     
        
class ActionCovidNews(Action):

    def name(self) -> Text:
        return "action_covid_news"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        #api_key = "ef44803195f1493ebc25c01d38d989f4"
        #newsapi = NewsApiClient(api_key=api_key)
 #       sources = newsapi.get_sources(country='in',q = "corona")
 #       sources = [x['id'] for x in sources['sources']]
        response_we_need = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=ef44803195f1493ebc25c01d38d989f4").json()
       
#        print(sources)
        data = pd.DataFrame(response_we_need['articles'])
        message = []
        for i in range(len(data)):
            message.append(data['title'][i])
        print(message)
        dispatcher.utter_message(text = "Top Highlights for the day are: ")
        for msg in message:
            dispatcher.utter_message(text = msg)
            dispatcher.utter_message(text = "\n")
        
        
        return []