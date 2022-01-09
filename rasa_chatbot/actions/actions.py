import time
from typing import Any, Dict, List, Text

from ivy.ivy import IvyServer
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher

from .course import Courses
from .stt_tts import Stt, Tts


class ActionIvy(IvyServer):
    def __init__(self):
        IvyServer.__init__(self, "ActionIvy")
        self.start("127.255.255.255:2010")


class Maison(Action):
    def name(self) -> Text:
        return "action_maison"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        connexion = ActionIvy()
        time.sleep(1)
        tts = Tts()
        slots = tracker.current_slot_values()
        if slots["action_maison"] == None:
            tts.say("Je n'ai pas compris.")
        elif "allum" in slots["action_maison"]:
            if slots["lumiere"] == "lumière" or slots["lumiere"] == "lumières":
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
            if slots["lumiere"] == "lumière" or slots["lumiere"] == "lumières":
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
        elif (
            "met" in slots["action_maison"]
            or "règ" in slots["action_maison"]
            or "rég" in slots["action_maison"]
        ):
            try:
                temperature = int(float(slots["temperature"]))
                connexion.send_msg(
                    "MAISON device=temperature action=" + str(temperature)
                )
                tts.say(
                    "Le chauffage est maintenant réglé sur "
                    + str(temperature)
                    + " degré."
                )
            except:
                tts.say("Je n'ai pas compris.")
        else:
            tts.say("Je n'ai pas compris.")

        connexion.stop()
        return [AllSlotsReset()]


class ListeCourses(Action):
    def name(self) -> Text:
        return "action_liste_courses"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        connexion = ActionIvy()
        time.sleep(1)
        tts = Tts()
        slots = tracker.current_slot_values()

        liste_courses = Courses()
        if "ajouter" in slots["action_course"]:
            if slots["quantite"] == None:
                slots["quantite"] = ["1" for i in range(len(slots["article"]))]
            if len(slots["quantite"]) != len(slots["article"]):
                slots["quantite"] = ["1" for i in range(len(slots["article"]))]
            for i in range(len(slots["article"])):
                liste_courses.add(slots["article"][i], int(slots["quantite"][i]), "")
            lc = liste_courses.get()
            liste_ivy = ""
            for item in lc:
                if liste_ivy != "":
                    liste_ivy += " "
                liste_ivy = liste_ivy + str(item[0]) + "," + item[1]
            connexion.send_msg("MAISON device=liste action=" + liste_ivy)
            tts.say("La liste des courses a été mise à jour.")
        elif "supprimer" in slots["action_course"]:
            liste_courses.reset()
            connexion.send_msg("MAISON device=liste action=")
            tts.say("La liste des courses a été effacée.")
        elif "énoncer" in slots["action_course"]:
            lc = liste_courses.get()
            if len(lc) == 0:
                tts.say("La liste est vide pour le moment.")
            else:
                tts.say("Voici votre liste des courses.")
                for item in lc:
                    tts.say(str(item[0]) + item[1])
        else:
            tts.say("Je n'ai pas compris.")

        connexion.stop()
        return [AllSlotsReset()]


class Message(Action):
    def name(self) -> Text:
        return "action_message"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        connexion = ActionIvy()
        time.sleep(1)
        tts = Tts()
        stt = Stt()
        slots = tracker.current_slot_values()

        if slots["envoyer"] != None:
            if "papa" in slots["destinataire"]:
                message = stt.enregistrer_message()
                if message != "Error":
                    tts.say("J'ai envoyé " + message + " à papa.")
                    # TODO WHATSAPP
                    connexion.send_msg("MAISON device=papa action=message")
            elif "maman" in slots["destinataire"]:
                message = stt.enregistrer_message()
                if message != "Error":
                    tts.say("J'ai envoyé " + message + " à maman.")
                    # TODO WHATSAPP
                    connexion.send_msg("MAISON device=maman action=message")
            else:
                tts.say("Je n'ai pas compris.")
        else:
            tts.say("Je n'ai pas compris.")

        connexion.stop()
        return [AllSlotsReset()]
