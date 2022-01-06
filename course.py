#Classe représentant un objet de la liste des courses
#Possède un nom, une quantité et des détails

class Course:

    def __init__(self,name,quantite,details):
        self.nom = name
        self.qte = quantite
        self.details = details

    def getNom(self):
        return self.nom

    def getQuantite(self):
        return self.qte

    def getDetails(self):
        return self.details
    
    def __str__(self):
        if self.details is None:            
            return self.getNom() + " quantité : " +str(self.getQuantite())
        else:
            return self.getNom() + " quantité :" +str(self.getQuantite()) + ", " + self.getDetails()