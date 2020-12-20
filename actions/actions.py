# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from sql_leave_balance.select_data import selectUserLeave

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        uid = int(tracker.get_slot('uid'))  # validate the user..
        leave = tracker.get_slot('leave')
        res = selectUserLeave(uid, leave)
        output = "You are left with {}/5 {}s ".format(res, leave)
        dispatcher.utter_message(text=output)

        return []
