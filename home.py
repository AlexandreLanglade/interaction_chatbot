from ivy.ivy import IvyServer
import pygame
import sys

class Maison(IvyServer):
    def __init__(self):
        IvyServer.__init__(self,'Maison')
        self.start('127.255.255.255:2010')
        self.bind_msg(self.update, '^MAISON device=(.*) action=(.*)')
        self.lampe_salon = False
        self.lampe_chambre = False
        self.radiateur = False
        self.temperature = 19
        self.liste_courses = []
        self.tel_papa = 0
        self.tel_maman = 0
    
    def update(self, agent_name, device, action):
        """
        Messages possibles:
        - MAISON device=salon action=on : allume la lumière du salon
        - MAISON device=salon action=off : eteint la lumière du salon
        - MAISON device=chambre action=on
        - MAISON device=chambre action=off
        - MAISON device=radiateur action=on
        - MAISON device=radiateur action=off
        - MAISON device=temperature action=x : règle la température du radiateur à x°C
        - MAISON device=maman action=message : ajoute un message sur le tel de maman
        - MAISON device=papa action=message : ajoute un message sur le tel de papa
        - MAISON device=liste action=x : ajoute l'item x à la liste des courses
        """
        if device == "salon":
            if action == "on":
                self.lampe_salon = True
                return
            elif action == "off":
                self.lampe_salon = False
                return
        elif device == "chambre":
            if action == "on":
                self.lampe_chambre = True
                return
            elif action == "off":
                self.lampe_chambre = False
                return
        elif device == "radiateur":
            if action == "on":
                self.radiateur = True
                return
            elif action == "off":
                self.radiateur = False
                return
        elif device == "temperature":
            try:
                nouvelle_temperature = int(action)
                self.temperature = nouvelle_temperature
            except:
                print("--> Erreur lors du cast en int de la température.")
            return
        elif device == "maman" and action == "message":
            self.tel_maman += 1
            return
        elif device == "papa" and action == "message":
            self.tel_papa += 1
            return
        elif device == "liste":
            self.liste_courses.append(action)
            return
        print("Le message est incorrect et n'a pas été traité : ", device, action)


if __name__ == "__main__":
    maison = Maison()
    pygame.init()
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((977,646))
    pygame.display.set_caption("La Maison (The house en anglais)")

    # background maison
    background = pygame.image.load("img/maison.jpg")

    # effet noir lampe eteinte
    salle_eteinte = pygame.Surface((258,149))
    salle_eteinte.fill((0,0,0))

    transparence_chambre = 0
    transparence_salon = 0

    # ecriture température du radiateur
    font = pygame.font.SysFont("comicsansms", 14)

    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                maison.stop()
                sys.exit()

        screen.blit(background, (0,0))

        if maison.lampe_chambre == False:
            salle_eteinte.set_alpha(transparence_chambre)
            screen.blit(salle_eteinte, (225,212))
            if transparence_chambre <= 200:
                transparence_chambre += 5
        elif maison.lampe_chambre == True:
            transparence_chambre = 0
            
        if maison.lampe_salon == False:
            salle_eteinte.set_alpha(transparence_salon)
            screen.blit(salle_eteinte, (225,405))
            if transparence_salon <= 200:
                transparence_salon += 5
        elif maison.lampe_salon == True:
            transparence_salon = 0
        
        if maison.radiateur == True:
            pygame.draw.circle(screen,(255,0,0),(370,299),4)
        temperature_affichage = font.render(str(maison.temperature), True, (0,0,0))
        screen.blit(temperature_affichage,(419,297))

        if maison.tel_maman != 0:
            #notif maman gauche
            pass
        if maison.tel_papa != 0:
            #notif maman gauche
            pass

        if len(maison.liste_courses) > 0:
            #afficher liste course
            pass

        pygame.display.update()
        fps_clock.tick(30)