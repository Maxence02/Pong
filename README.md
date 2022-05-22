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
  ![image](https://user-images.githubusercontent.com/90564884/161870045-68a92e9d-5db0-4484-a8cf-6bf203e9048a.png)


journal :
  permier code établi en environ 2h avec peu de difficulté car ressemblant beaucoup au projet precedent ( snake ). ( 06/04 )
  fin du programme Pong sur un seul ordinateur sans grande difficulté car je connaissais déjà beaucoup le module pygame car j'ai déjà fait un snake avec. ( 15/05 )
  fin du programme sur deux ordinateurs avec de grosse difficulté sur le module socket que je ne connaissais pas mais cela m'a permis de mieux voir comment les 
  ordinateur communique entre eux. ( 23/05 )
