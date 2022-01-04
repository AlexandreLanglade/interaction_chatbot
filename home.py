from ivy.ivy import IvyServer
import pygame
import sys

class Maison(IvyServer):
    def __init__(self):
        IvyServer.__init__(self,'Maison')
        self.start('127.255.255.255:2010')
        #self.bind_msg(self.callback, '^??? (.*)')
        self.lampe_salon = False
        self.lampe_chambre = False
        self.radiateur = False
        self.temperature = 19
        self.liste_courses = []
        self.tel_papa = 0
        self.tel_maman = 0


if __name__ == "__main__":
    maison = Maison()
    pygame.init()
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode((977,646))
    pygame.display.set_caption("La Maison (The house en anglais)")

    # background maison
    background = pygame.image.load("img/maison.jpg")
    screen.blit(background, (0,0))

    # effet noir lampe eteinte
    salle_eteinte = pygame.Surface((258,149))
    salle_eteinte.set_alpha(5)
    salle_eteinte.fill((0,0,0))

    iteration_chambre = 0
    iteration_salon = 0

    # ecriture température du radiateur
    font = pygame.font.SysFont("comicsansms", 14)

    while True:
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
                maison.stop()
                sys.exit()

        if maison.lampe_chambre == False and iteration_chambre <= 45:
            screen.blit(salle_eteinte, (225,212))
            iteration_chambre += 1
        elif maison.lampe_chambre == True:
            iteration_chambre = 0
            
        if maison.lampe_salon == False and iteration_salon <= 45:
            screen.blit(salle_eteinte, (225,405))
            iteration_salon += 1
        elif maison.lampe_salon == True:
            iteration_salon = 0
        
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