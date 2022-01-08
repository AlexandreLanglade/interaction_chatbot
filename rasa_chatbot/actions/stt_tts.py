import pyttsx3
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
                            # TODO ENVOI DE LA PAROLE A RASA ?
                            return parole2
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
