# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import random
class ActionCheckMealCategory(Action):

    def name(self):
        return "action_check_meal_category"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # setting meal category
        meal_category = {
            'dumplings': ['F7-八方雲集'],
            'rice': ['F7-高雄空廚'],
            'juice': ['F2&5-果汁熊', 'F3-果真新鮮', 'F18-果真新鮮'],
            'coffee': ['F7-Starbucks', 'F7-Louisa', 'F12-Starbucks'],
            'bread': ['F15A-品麵包', 'FAB14P5-多那之', 'F15B-哈拉烘焙'],
        }
        try:
            category = tracker.latest_message['entities'][0]['value']
            if category in meal_category:
                place = random.choice(meal_category[category])
                dispatcher.utter_message(response="utter_place_found", place=place, category=category)
            else:
                dispatcher.utter_message(response="utter_place_not_found")
        except:
            dispatcher.utter_message(response="utter_place_not_found")
        return []

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
