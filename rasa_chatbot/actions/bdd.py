import sqlite3


# base de données SQLlite contenant la liste des courses
# La table course contient des données de la forme :
# -nom (id unique)
# -quantité
# -details (exemple pour du lait, demi ecreme)
class Database:
    def add(self, nom, qte, details):
        if details is None:
            details = ""
        try:
            conn = sqlite3.connect("ma_base.db")
            cursor = conn.cursor()
            cursor.execute(
                """INSERT INTO course(name, qte, details) VALUES(?, ?, ?)""",
                (nom, qte, details),
            )
            conn.commit()
        except sqlite3.IntegrityError:  # cas ou l'ingredient existe deja, on ajoute la quantite
            conn = sqlite3.connect("ma_base.db")
            cursor = conn.cursor()
            # récupérer la quantité existante
            cursor.execute("""SELECT qte FROM course WHERE name= ? """, (nom,))
            quantite = cursor.fetchall()
            quantite = quantite[0][0]
            # ajouter la quantité à celle existante
            cursor.execute(
                """UPDATE course SET qte = ? WHERE name = ?""", (quantite + qte, nom)
            )
            conn.commit()

    # data en entrée = data = [("raisins", 3, ""),("pain", 2, ""),("lait",6,"demi-ecreme")]
    def add_multiple(self, data):
        try:
            conn = sqlite3.connect("ma_base.db")
            cursor = conn.cursor()
            cursor.executemany("""INSERT INTO course VALUES(?, ?, ?)""", data)
            conn.commit()
        except sqlite3.IntegrityError:  # cas ou l'ingredient existe deja, on ajoute la quantite
            print("Des ingrédients identiques sont déja présents dans la liste")

    def select(self):
        conn = sqlite3.connect("ma_base.db")
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM course""")
        course = cursor.fetchall()
        return course

    def reset(self):
        conn = sqlite3.connect("ma_base.db")
        cursor = conn.cursor()
        cursor.execute("""DROP TABLE course""")
        conn.commit()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS course(
          name TEXT PRIMARY KEY,
          qte INTERGER,
          details TEXT)"""
        )
        conn.commit()

    def delete(self, nom):
        conn = sqlite3.connect("ma_base.db")
        cursor = conn.cursor()
        cursor.execute("""DELETE FROM course where name = ?""", (nom,))
        conn.commit()
