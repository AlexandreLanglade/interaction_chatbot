import json

import pyttsx3
import requests
import speech_recognition as sr


class Tts:
    def say(self, texte):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(texte)
        engine.runAndWait()


class Stt:
    def google_stt(self):
        text_to_speech = Tts()
        micro = sr.Microphone()
        while True:
            recognizer = sr.Recognizer()
            with micro as source:
                audio = recognizer.listen(source, phrase_time_limit=3)
                try:
                    parole = recognizer.recognize_google(audio, language="fr-FR")
                    if parole == "ok Google":
                        text_to_speech.say("Bonjour, que puis-je pour vous ?")
                        try:
                            audio2 = recognizer.listen(source)
                            parole2 = recognizer.recognize_google(
                                audio2, language="fr-FR"
                            )
                            print(parole2)
                            self.envoyer_rasa(parole2)
                        except:
                            text_to_speech.say(
                                "Je n'ai pas compris, relancez Ok Google"
                            )
                except:
                    print("Sleep, pas d'activation detectée")

    def enregistrer_message(self):
        text_to_speech = Tts()
        micro = sr.Microphone()
        recognizer = sr.Recognizer()
        text_to_speech.say("Je vous écoute.")
        with micro as source:
            try:
                audio = recognizer.listen(source, phrase_time_limit=3)
                parole = recognizer.recognize_google(audio, language="fr-FR")
                return parole
            except:
                text_to_speech.say("Je n'ai pas compris le message à envoyer.")
                return "Error"

    def envoyer_rasa(self,parole):
         #ENVOI DE LA PAROLE A RASA                                                                    
        url = 'http://localhost:5005/webhooks/myio/webhook'
        payload = {'sender': 'test_user','message': parole,'metadata': {}}
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(payload), headers=headers)

if __name__ == "__main__":
    #Entrée vocale de l'utilisateur
    speech_to_text = Stt()
    parole = speech_to_text.google_stt()