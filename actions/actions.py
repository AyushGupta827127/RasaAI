# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
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


from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random

class ActionHandleRepeatedQueries(Action):
    def name(self) -> str:
        return "action_handle_repeated_queries"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        last_question = tracker.latest_message.get('text')
        
        # Check if the user has asked the same question repeatedly
        if 'compliance policy' in last_question.lower():
            response = random.choice([
                "Our compliance policy is updated annually. It includes procedures for data protection and risk management.",
                "We take compliance seriously. The policy outlines security and privacy protocols.",
                "Compliance is a critical aspect of our operations, and it includes regulatory requirements and audits."
            ])
        elif 'tax regulation' in last_question.lower():
            response = random.choice([
                "Tax regulations change every year. The current tax rate for businesses is 21%.",
                "The tax compliance requirements for this year include specific deductions and reporting rules.",
                "This year's tax regulations require businesses to report income by the end of the fiscal year."
            ])
        elif 'deadline' in last_question.lower():
            response = random.choice([
                "The compliance deadline is December 31st. Make sure to submit everything by then.",
                "The deadline for compliance reports is the last day of this year, December 31st.",
                "You need to submit your compliance documents by the end of the fiscal year, usually December 31st."
            ])
        else:
            response = "Sorry, I didn't understand that. Could you please clarify your question?"
        
        dispatcher.utter_message(text=response)
        return []

