# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List, Union
 


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class formulario_saude(FormAction):
 
    def name(self) -> Text:
        return "formulario_saude"

    @staticmethod
    def required_slots(tracker):

        if  tracker.get_slot("confirmar_exercicio") == True:
            return ["confirmar_exercicio", "exercicio", "dormir", "dieta", "stress", "objetivo"]
        else:
            return ["confirmar_exercicio", "dormir", "dieta", "stress", "objetivo"]


    def submit(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
        ) -> List[Dict]:
        return []
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return{
            "confirmar_exercicio":[
                self.from_intent(intent="afirmação", value=True),
                self.from_intent(intent="negação", value=False),
                self.from_intent(intent="informação", value=True),
            ],
            "dormir":[
                self.from_entity(entity="sono"),
                self.from_intent(intent="negação", value="None"),
            ],
            "diet":[
                self.from_text(intent="informação"),
                self.from_text(intent="afirmação"),
                self.from_text(intent="negação"),
            ],
            "objetivo":[
                self.from_text(intent="informação"),
            ],
        }