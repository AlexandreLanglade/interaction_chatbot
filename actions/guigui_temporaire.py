"""
ajouter:

actions:
  - action_search_concerts
  - action_search_venues
  - action_show_concert_reviews
  - action_show_venue_reviews
  - action_set_music_preference

dans le domain
"""

from bdd import database
from stt_tts import Tts,stt

from course import *

#Cette classe représente l'ensemble des actions pouvant être appelée par le chatbot RASA
class actions:

################## GESTION DE LA LISTE DES COURSES ###################

    #Cette fonction permet de lister la liste des courses complète pour l'interface graphique
    def envoyer_liste_course(self):
        db = database()
        liste = db.select()
        liste_ingredient = []       
        #Envoyer l'état actuel de la base de données
        for (nom,qte,details) in liste:
            ingredient = Course(nom,qte,details)
            liste_ingredient.append(ingredient)
        #Envoi sur IVY
        ### !!!!!! ###
        print("Envoi sur IVY de la liste des courses actuelles pour l'interface graphique")

    #Cette fonction permet à l'assistant vocal de lire la liste des courses    
    def consultation_liste_course(self):
        db = database()
        liste = db.select()
        liste_ingredient = []        
        for (nom,qte,details) in liste:
            ingredient = Course(nom,qte,details)
            self.dire_message_oral(ingredient.__str__())

    #Cette fonction permet d'ajouter un élément dans la lsite des courses
    def ajouter_un_ingredient_course(self,nom,qte,details):
        db = database()
        db.add(nom,qte,details)
        ingredient = Course(nom,qte,details)        
        print("Ajout d'un ingrédient : ", ingredient)
        self.envoyer_liste_course()

    #Cette fonction permet d'ajouter une liste d'élément dans la lsite des courses
    def ajouter_plusieurs_ingredients_course(self,data):
        db = database()        
        db.add_multiple(data)
        liste_ingredient = []
        for (nom,qte,details) in data:
            ingredient = Course(nom,qte,details)
            liste_ingredient.append(ingredient.__str__())
        print("Ajout d'une liste d'ingrédients : ",liste_ingredient)        
        self.envoyer_liste_course()

    #Cette fonction vide la liste des courses dans son entièreté 
    def vider_liste_course(self):
        db=database()
        db.reset()
        print("Base de données vidée")
        self.envoyer_liste_course()

    #Cette fonction permet de retirer un élément de la liste
    def supprimer_un_element(self,nom):
        db=database()
        db.delete(nom)
        print("Ingrédient "+nom+" supprimé")
        self.envoyer_liste_course()

################### RETOUR ORAL POUR UTILISATEUR ###################

    def dire_message_oral(self,texte):
        text_to_speech = Tts()
        text_to_speech.python_tts(texte)

################### ACTION GESTION DES DEVICES ######################

    def allumer_lumiere(self,piece):
        #Envoi IVY pour l'interface
        #### !!! ####
        self.dire_message_oral("Lumière de la pièce " + piece + " activée")
    
    def eteindre_lumiere(self,piece):
        #Envoi IVY pour l'interface
        #### !!! ####
        self.dire_message_oral("Lumière de la pièce " + piece + " desactivée")

    def allumer_chauffage(self,piece,temperature):
        #Envoi IVY pour l'interface
        #### !!! ####
        self.dire_message_oral("Chauffage de la pièce " + piece + " fixé à " + str(temperature) + " degré")
    
    def eteindre_chauffage(self,piece):
        #Envoi IVY pour l'interface
        #### !!! ####
        self.dire_message_oral("Chauffage de la pièce " + piece + " éteind")

############### ENVOI MESSAGE TELEPHONE ################
########## TO DO #################
############### CONNEXION APPLICATION DE MESSAGERIE ###############
########## TO DO #################

if __name__ == "__main__":
    #Entrée vocale de l'utilisateur
    speech_to_text = stt()
    parole = speech_to_text.google_stt()
    print("Parole envoyée à RASA: ", parole)    
    #Traitement RASA
    
    #simuler les infos reconnues par rasa
    act = actions()
    #data = [("banane ",6 , ""),("pain", 2, ""),("lait",6,"demi-ecreme")]
    #act.vider_liste_course()  
    #act.ajouter_plusieurs_ingredients_course(data)
    #act.supprimer_un_element("pains")
    act.consultation_liste_course()
    
    
