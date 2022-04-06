import pygame
import sys
from joueur import joueur

class Jeu :
    
    def __init__(self) :
        
        self.ecran = pygame.display.set_mode((900,500))
        pygame.display.set_caption("Jeu de Pong")
        self.jeu_encours = True
        self.joueur_1_x, self.joueur_1_y = 20, 250
        self.joueur_2_x, self.joueur_2_y = 860, 250
        self.joueur_taille = [20, 80]
        self.vitesse_y_1, self.vitesse_y_2 = 0, 0
        self.clock = pygame.time.Clock()
        self.joueur_1 = joueur(self.joueur_1_x, self.joueur_1_y, self.joueur_taille)
        self.joueur_2 = joueur(self.joueur_2_x, self.joueur_2_y, self.joueur_taille)
        self.rect = pygame.Rect(0, 0, 900, 500)
        
    def boucle_principale(self):
        
        while self.jeu_encours :
            
             for event in pygame.event.get():
                 
                 if event.type == pygame.QUIT:
                     sys.exit()
                     
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_UP:
                         self.vitesse_y_1 = -10
                     if event.key == pygame.K_DOWN:
                         self.vitesse_y_1 = 10
                         
                     if event.key == pygame.K_z:
                         self.vitesse_y_2 = -10
                     if event.key == pygame.K_s:
                         self.vitesse_y_2 = 10
                         
                 if event.type == pygame.KEYUP :
                     if event.key == pygame.K_UP:
                         self.vitesse_y_1 = 0
                     if event.key == pygame.K_DOWN:
                         self.vitesse_y_1 = 0
                         
                     if event.key == pygame.K_z:
                         self.vitesse_y_2 = 0
                     if event.key == pygame.K_s:
                         self.vitesse_y_2 = 0
                         
             self.joueur_1.mouvement(self.vitesse_y_1)
             self.joueur_2.mouvement(self.vitesse_y_2)
             self.joueur_1.rect.clamp_ip(self.rect)  #bloque le joueur au limite de l'ecran
             self.joueur_2.rect.clamp_ip(self.rect)  #bloque le joueur au limite de l'ecran
             
             self.ecran.fill((50, 50, 50))
             self.joueur_1.afficher(self.ecran)
             self.joueur_2.afficher(self.ecran)
             pygame.display.flip()
             self.clock.tick(30)

if __name__ == '__main__':
    pygame.init()
    Jeu().boucle_principale()
    pygame.quit()