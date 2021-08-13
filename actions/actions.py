# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime as dt
import random

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

class ActionOrderFoodButton(Action):

    def name(self):
        return "action_order_food"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_order_food")
        return []

class ActionFindFoodButton(Action):

    def name(self):
        return "action_find_food"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_find_food")
        return []

class ActionFood(Action):

    def name(self) -> Text:
        return "action_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        parking_resources = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "dims":{
                    "width": 100,
                    "height": 100
                },
                "elements": [{
                    "title": "黑胡椒雞胸餐盒(無米飯)",
                    "subtitle": "價格 : 85元 取餐區 : 1F茶水間 廠商 : 頗微康",
                    "image_url": "static/黑胡椒雞胸餐盒.png",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "訂餐",
                            "type": "postback",
                            "payload": "/button_order_food",
                        },
                        {
                            "title": "查詢更多餐點",
                            "type": "postback",
                            "payload": "/button_find_food",
                        }
                    ]
                },
                {
                    "title": "LOUISA COFFEE 熱壓吐司",
                    "subtitle": "價格 : xx元 取餐區 : xxx 廠商 : 路易莎(為公司內餐廳之餐點)",
                    "image_url": "static/Louis-熱壓吐司.jfif",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "訂餐",
                            "type": "postback",
                            "payload": "/button_order_food",
                        },
                        {
                            "title": "查詢更多餐點",
                            "type": "postback",
                            "payload": "/button_find_food",
                        }
                    ]
                }
                ]
            }
        }

        dispatcher.utter_message(attachment=parking_resources)
        # dispatcher.utter_custom_json(parking_resources)
        return []



class ActionButtonSpace(Action):

    def name(self):
        return "action_button_restaurant"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_restaurant")
        return []


class ActionCarousel(Action):
    def name(self) -> Text:
        return "action_restaurants"
 
    def run(self, dispatcher, tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        restaurants = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": "四海遊龍",
                        "subtitle": "2廠B1",
                        "image_url": "static/p1.jpg",
                        "dims": {
                            "width": 50,
                            "height": 50
                        },
                        "buttons": [
                            {
                                "title": "鍋貼 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "水餃 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "乾麵 $65",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "牛肉湯餃 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "晶記燒臘",
                        "subtitle": "2廠B1",
                        "image_url": "static/B1.jpg",
                        "dims": {
                            "width": 50,
                            "height": 50
                        },
                        "buttons": [
                            {
                                "title": "燒鴨飯 $75",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "燒肉飯 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "烤鴨飯 $75",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "排骨飯 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            }
                        ]
                    },
                    {
                        "title": "竹美行",
                        "subtitle": "2廠B1",
                        "image_url": "static/B1.jpg",
                        "buttons": [
                            {
                                "title": "滷肉飯 $65",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "排骨便當 $75",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "乾麵 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            },
                            {
                                "title": "炒米粉 $70",
                                "payload": "/button_restaurant",
                                "type": "postback"
                            }
                        ]
                    },
                ]
            }
        }
        dispatcher.utter_message(attachment=restaurants)
        return []

class ActionCheckMealCategory(Action):

    def name(self):
        return "action_check_meal_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # setting meal category
        meal_category = {
            'dumplings': ['F7-八方雲集'],
            'rice': ['F7-高雄空廚', 'F7-鬍鬚張'],
            'juice': ['F2&5-果汁熊', 'F3-果真新鮮', 'F18-果真新鮮'],
            'coffee': ['F7-Starbucks', 'F7-Louisa', 'F12-Starbucks'],
            'bread': ['F15A-品麵包', 'FAB14P5-多那之', 'F15B-哈拉烘焙'],
        }
        try:
            category = tracker.latest_message['entities'][0]['value']
            if category in meal_category:
                place = random.choice(meal_category[category])
                dispatcher.utter_message(
                    response="utter_place_found", place=place, category=category)
            else:
                dispatcher.utter_message(
                    response="utter_place_not_found")
        except:
            dispatcher.utter_message(response="utter_place_not_found")
        return []

class ActionButtonSpace(Action):

    def name(self):
        return "action_button_parking_space"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_parking_space")
        return []

class ActionButtonParkingSpaceReserve(Action):

    def name(self):
        return "action_button_parking_space_reserve"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_parking_space_reserve")
        return []

class ActionQuickPath(Action):

    def name(self):
        return "action_quick_path"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_quick_path")
        return []

class ActionParkingSpace(Action):

    def name(self) -> Text:
        return "action_show_parking_space"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        parking_resources = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "dims":{
                    "width": 100,
                    "height": 100
                },
                "elements": [{
                    "title": "PARKING SPACE B1",
                    "subtitle": "10 SPACE LEFT",
                    "image_url": "static/B1.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Empty space",
                            "type": "postback",
                            "payload": "/button_parking_space"
                        },

                        {
                            "title": "Reserve ",
                            "type": "postback",
                            "payload": "/button_parking_space_reserve"
                        }
                        
                    
                    ]
                },
                {
                    "title": "PARKING SPACE B2",
                    # "subtitle": "FIND SPACE, SAVE TIEM",
                    "subtitle": "51 SPACE LEFT",
                    "image_url": "static/B2.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Empty space",
                            "type": "postback",
                            "payload": "/greet"
                        },

                        {
                            "title": "Reserve",
                            "type": "postback",
                            "payload": "/affirm"
                        }
                    ]
                },
                 {
                    "title": "PARKING SPACE B3",
                    "subtitle": "75 SPACE LEFT",
                    "image_url": "static/B3.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Empty space",
                            "type": "postback",
                            "payload": "/greet"
                        },

                        {
                            "title": "B2",
                            "type": "postback",
                            "payload": "/goodbye"
                        }
                    ]
                }
                ]
            }
        }

        # dispatcher.utter_message(attachment=parking_resources)
        dispatcher.utter_message(attachment=parking_resources)
        return []

class ActionShuttleBus(Action):

    def name(self) -> Text:
        return "action_shuttle_bus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        shuttle_bus = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "dims":{
                    "width": 100,
                    "height": 100
                },
                "elements": [{
                    "title": "Hsinchu Site",
                    # "subtitle": "10 SPACE LEFT",
                    "image_url": "static/shuttle_bus_Hsinchu_site.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Timetable",
                            "type": "postback",
                            "payload": "/request_timetable"
                        },

                        {
                            "title": "Lastest shuttle bus",
                            "type": "postback",
                            "payload": "/request_latest_shuttleBus"
                        }
                        
                    
                    ]
                },
                {
                    "title": "Taichung Site",
                    # "subtitle": "FIND SPACE, SAVE TIEM",
                    # "subtitle": "51 SPACE LEFT",
                    "image_url": "static/shuttle_bus_Taichung_site.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Timetable",
                            "type": "postback",
                            "payload": "/request_timetable"
                        },

                        {
                            "title": "Lastest shuttle bus",
                            "type": "postback",
                            "payload": "/request_latest_shuttleBus"
                        }
                    ]
                },
                 {
                    "title": "Tainan Site",
                    # "subtitle": "75 SPACE LEFT",
                    "image_url": "static/shuttle_bus_Tainan_site.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Timetable",
                            "type": "postback",
                            "payload": "/request_timetable"
                        },

                        {
                            "title": "Lastest shuttle bus",
                            "type": "postback",
                            "payload": "/request_latest_shuttleBus"
                        }
                    ]
                }
                ]
            }
        }

        dispatcher.utter_message(attachment=shuttle_bus)
        return []

class ShuttoleBusePathForm(FormValidationAction):
    def name(self) -> Text:
        return "action_shuttlebus_path_form"

    def shuttle_bus_path_initiating_station(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"initiating_station": slot_value}

    def shuttle_bus_path_terminal_station(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"terminal_station": slot_value}
    
class ShuttoleBusePathTimeForm(FormValidationAction):
    def name(self) -> Text:
        return "action_shuttlebus_path_time_form"

    def shuttle_bus_path_initiating_station(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"initiating_station": slot_value}

    def shuttle_bus_path_terminal_station(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"terminal_station": slot_value}

    def shuttle_bus_path_Departure_time_hour(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"Departure_time_hour": slot_value}

    def shuttle_bus_path_Departure_time_min(
        self, 
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
        ) -> Dict[Text, Any]:
        print(f"Initiating five = {slot_value} length={len(slot_value)}")
        return {"Departure_time_min": slot_value}

class Action2999Online(Action):

    def name(self):
        return "action_2999_online"
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_2999_online")
        return []
