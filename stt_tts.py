
import pyttsx3
import speech_recognition as sr

#classe permettant de réaliser le text to speech (retour à l'utilisateur)
class Tts:
    ###### AVEC GOOGLE (google text to speech) - online #######
    ###### METHODE OFFLINE ######
    def say(self, texte):
        engine = pyttsx3.init()
        engine.setProperty("rate", 150)
        engine.say(texte)
        engine.runAndWait()

################################################################################

#classe permettant de réaliser le speech to text (parole de l'utilisateur)
class stt:
    ##### AVEC GOOGLE (speech recognizer google) - online #####
    def google_stt(self):
        text_to_speech = tts()    
        micro = sr.Microphone() #utiliser le micro comme source
        parole=""
        i=1
        while(i<2):
            recognizer = sr.Recognizer()	
            with micro as source:
                audio = recognizer.listen(source,phrase_time_limit=3)
                try:
                    parole = recognizer.recognize_google(audio, language="fr-FR")
                    #print(parole)
                    if(parole == "ok Google"):
                        text_to_speech.python_tts("Bonjour, que puis-je pour vous ?")
                        try:                        
                            audio2 = recognizer.listen(source)                
                            parole2 = recognizer.recognize_google(audio2, language="fr-FR")                    
                            #print(parole2)
                            text_to_speech.python_tts("Vous avez dit : " + parole2)
                            #ENVOI DE LA PAROLE A RASA
                            ### !!!!!!!!!!!!!!!!!!!! ###
                            i=i+1
                            return parole2
                        except:
                            text_to_speech.python_tts("Je n'ai pas compris, relancez Ok Google")
                except:
                    print("Sleep, pas d'activation detectée")


   