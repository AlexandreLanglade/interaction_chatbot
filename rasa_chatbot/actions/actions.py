import time
from typing import Any, Dict, List, Text

from ivy.ivy import IvyServer
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from stt_tts import Tts


class ActionIvy(IvyServer):
    def __init__(self):
        IvyServer.__init__(self, "ActionIvy")
        self.start('127.255.255.255:2010')


class Maison(Action):
    def name(self) -> Text:
        return "action_maison"

    def run(self):
        """
        , dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        connexion = ActionIvy()
        time.sleep(1)
        tts = Tts()
        #slots = tracker.current_slot_values()
        slots = {"action_maison":"éteint","piece":"salon","chauffage":None,"lumiere":"lumière","temperature":None}
        if "allum" in slots["action_maison"]:
            if slots["lumiere"] == "lumière":
                if slots["piece"] == "salon":
                    connexion.send_msg("MAISON device=salon action=on")
                    tts.say("J'ai allumé la lumière du salon.")
                elif slots["piece"] == "chambre":
                    connexion.send_msg("MAISON device=chambre action=on")
                    tts.say("J'ai allumé la lumière de la chambre.")
                else:
                    connexion.send_msg("MAISON device=salon action=on")
                    connexion.send_msg("MAISON device=chambre action=on")
                    tts.say("J'ai allumé les lumières.")
            elif slots["chauffage"] == "chauffage":
                connexion.send_msg("MAISON device=radiateur action=on")
                tts.say("J'ai allumé le chauffage.")
            else:
                tts.say("Je n'ai pas compris.")
        elif "étein" in slots["action_maison"]:
            if slots["lumiere"] == "lumière":
                if slots["piece"] == "salon":
                    connexion.send_msg("MAISON device=salon action=off")
                    tts.say("J'ai éteint la lumière du salon.")
                elif slots["piece"] == "chambre":
                    connexion.send_msg("MAISON device=chambre action=off")
                    tts.say("J'ai éteint la lumière de la chambre.")
                else:
                    connexion.send_msg("MAISON device=salon action=off")
                    connexion.send_msg("MAISON device=chambre action=off")
                    tts.say("J'ai éteint les lumières.")
            elif slots["chauffage"] == "chauffage":
                connexion.send_msg("MAISON device=radiateur action=off")
                tts.say("J'ai éteint le chauffage.")
            else:
                tts.say("Je n'ai pas compris.")
        elif "met" in slots["action_maison"] or "règ" in slots["action_maison"]:
            try:
                temperature = int(float(slots["temperature"]))
                connexion.send_msg("MAISON device=temperature action=" + str(temperature))
                tts.say("Le chauffage est maintenant réglé sur " + str(temperature) + " degré.")
            except:
                tts.say("Je n'ai pas compris.")
        else:
            tts.say("Je n'ai pas compris.")

        connexion.stop()
        return [AllSlotsReset()]


class ListeCourses(Action):
    def name(self) -> Text:
        return "action_liste_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]


class Message(Action):
    def name(self) -> Text:
        return "action_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]
