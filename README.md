# Pong
création du jeu pong avec la bibliothèque pygame
j'hesite entre deux une quil utilise la bibliotheque pygame simplement pour cree le jeu pong sur un ordinateur ou 
alors quelque chose d'autre que je chercherais qui me permetrais de jouer sur deux ordinateur different 

je vais donc devoir creer ma balle puis mon personnage ( une barre dans le jeu ) et 
créer un serveur.

``` pyton
Barre.py() :  
  __init__(self) :  
  mouvement(self, vitesse):
  afficher(self, surface):
  
client.py() :  
  __init__(self) : 
  boucle_principale(self)
  creer_message(self, font, message, message_rectangle, couleur):
  recevoir_donnees(self):
  creer_un_thread(self, cible):
   
balle() :
   __init__(self, x:int, y:int, rayon:int, direction:int) :
  mouvement(self, vitesse_x:int, vitesse_y:int) :
  afficher(self, surface:list) :
  
 serveur.py() :  
  __init__(self) :  
  boucle_principale(self)
  changement_balle_direction(self, vitesse, angle):
  creer_message(self, font, message, message_rectangle, couleur):
  attendre_la_connection(self):
  recevoir_donnees(self):
  creer_un_thread(self, cible):
  
 ``` 
  journal :
  permier code établi en environ 2h avec peu de difficulté car ressemblant beaucoup au projet precedent. (06/04)
  ![image](https://user-images.githubusercontent.com/90564884/161870045-68a92e9d-5db0-4484-a8cf-6bf203e9048a.png)
