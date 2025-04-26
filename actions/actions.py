from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from datetime import datetime

class ActionInfoContato(Action):
    def name(self) -> Text:
        return "action_info_contato"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Você pode entrar em contato conosco pelo telefone (16) 99999-9999 ou pelo e-mail contato@ericktech.com.")
        return []

class ActionCheckHorario(Action):
    def name(self) -> Text:
        return "action_check_horario"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dia = next(tracker.get_latest_entity_values("dia"), None)
        agora = datetime.now()
        hora = agora.hour
        dia_semana = agora.strftime("%A")

        aberto = 8 <= hora < 18
        dias_abertos = ["segunda", "terça", "quarta", "quinta", "sexta"]

        if dia:
            if dia.lower() in dias_abertos:
                dispatcher.utter_message(text=f"Sim, estamos abertos na {dia} das 8h às 18h.")
            else:
                dispatcher.utter_message(text=f"Não, não abrimos na {dia}. Nosso horário é de segunda a sexta, das 8h às 18h.")
        else:
            if aberto:
                dispatcher.utter_message(text="Estamos abertos agora! Nosso horário vai até às 18h.")
            else:
                dispatcher.utter_message(text="Estamos fechados no momento. Funcionamos de segunda a sexta, das 8h às 18h.")

        return []
