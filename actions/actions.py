# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import datetime as dt
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"{dt.datetime.now()}")

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
        dispatcher.utter_custom_json(parking_resources)
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
                    "title": "Newa",
                    # "subtitle": "10 SPACE LEFT",
                    # "image_url": "static/B1.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Announcement",
                            "type": "postback",
                            "payload": "/button_parking_space"
                        },

                        {
                            "title": "Lastest News",
                            "type": "postback",
                            "payload": "/button_parking_space_reserve"
                        }
                        
                    
                    ]
                },
                {
                    "title": "Transportation Service Introduction",
                    # "subtitle": "FIND SPACE, SAVE TIEM",
                    # "subtitle": "51 SPACE LEFT",
                    # "image_url": "static/B2.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Shift 4-2 Commuting Bus",
                            "type": "postback",
                            "payload": "/greet"
                        },

                        {
                            "title": "Inter-Site buinesses Bus",
                            "type": "postback",
                            "payload": "/affirm"
                        },
                        {
                            "title": "Inter-Fab Shuttle Bus",
                            "type": "/greet",
                            "payload": "/affrim"
                        }
                    ]
                },
                 {
                    "title": "Reservation",
                    # "subtitle": "75 SPACE LEFT",
                    # "image_url": "static/B3.jpg",
                    "dims": {
                        "width": 50,
                        "height": 50
                    },
                    "buttons": [
                        {
                            "title": "Online Reservation",
                            "type": "postback",
                            "payload": "/greet"
                        },

                        {
                            "title": "Search Reservation Record",
                            "type": "postback",
                            "payload": "/goodbye"
                        }
                    ]
                }
                ]
            }
        }

        dispatcher.utter_message(attachment=shuttle_bus)
        return []

class InterFabShuttleBus(FormAction):
    def name(self):
        return "inter_fab_shuttle_bus"
    
    def required_slots(self, tracker) -> List[Text]:
        return ["TSMC_site","inter_fab_shuttle_bus_initial_station","inter_fab_shuttle_bus_final_station","inter_fab_shuttle_bus_hours","inter_fab_shuttle_bus_mins"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "TSMC site": [
                self.from_text(),
            ],

            "inter_fab_shuttle_bus_initial_station": [
                self.from_text(),
            ],

            "inter_fab_shuttle_bus_final_station": [
                self.from_text(),
            ],

            "inter_fab_shuttle_bus_hours": [
                self.from_text(),
            ],
            
            "inter_fab_shuttle_bus_mins": [
                self.from_text(),
            ],
        }
    # def submit(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> List[Dict]:
    # dispatcher.utter_message("Thank you for your patience")
    
    # return []