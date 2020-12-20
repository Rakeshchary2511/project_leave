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
from sql_leave_application.insert_application_data import insertApplicationData

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


class ActionLeaveApplication(Action):
    def name(self) -> Text:
        return "action_leave_application"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        uid = 0
        leave = ""
        start = ""
        end = ""
        reason = ""
        
        uid = int(tracker.get_slot('uid'))  # validate the user..
        leave = tracker.get_slot('leave')
        start = tracker.get_slot('start')
        end = tracker.get_slot('end')
        reason = tracker.get_slot('reason')
        # res = selectUserLeave(uid, leave)
        print(leave, start, end, reason)
        insertApplicationData(uid, leave, start, end, reason)
        output = "success"
        dispatcher.utter_message(text=output)
