from .bdd import Database


class Courses:
    def __init__(self):
        self.db = Database()

    def get(self):
        liste = self.db.select()
        liste_ingredient = []
        for (nom, qte, _) in liste:
            liste_ingredient.append((qte, nom))
        return liste_ingredient

    def add(self, nom, qte, details):
        self.db.add(nom, qte, details)

    def reset(self):
        self.db.reset()
