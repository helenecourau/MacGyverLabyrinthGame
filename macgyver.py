# -*- coding: Utf-8 -*
import pygame
from pygame.locals import *
import random

from classes import *
from constantes import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

macgyver = pygame.image.load(image_macgyver)
pygame.display.set_icon(macgyver)

#Titre
pygame.display.set_caption(titre_fenetre)


#BOUCLE PRINCIPALE
continuer = 1
while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_fond).convert()
	fenetre.blit(accueil, (0,0))
	lab = Map(fichier_lab)
	lab.generer()
	lab.afficher(fenetre)

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	
	#Limitation de vitesse de la boucle
	pygame.time.Clock().tick(30)
	
	for event in pygame.event.get():
		
		#Si l'utilisateur quitte, on met les variables 
		#de boucle à 0 pour n'en parcourir aucune et fermer
		if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
			continuer_jeu = 0
			continuer = 0

	#Création de MacGyver
	macGyver = MacGyver("images/MacGyver.png", "images/MacGyver.png", "images/MacGyver.png", "images/MacGyver.png", lab)

	#Création des objets
	seringue = Objet("images/seringue.png", lab)
	seringue.positionner()

	#BOUCLE DE JEU
	pygame.key.set_repeat(400, 30)
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					macGyver.deplacer('droite')
				elif event.key == K_LEFT:
					macGyver.deplacer('gauche')
				elif event.key == K_UP:
					macGyver.deplacer('haut')
				elif event.key == K_DOWN:
					macGyver.deplacer('bas')			
			
		#Affichages aux nouvelles positions
		fenetre.blit(accueil, (0,0))
		lab.afficher(fenetre)
		fenetre.blit(macGyver.direction, (macGyver.x, macGyver.y))
		fenetre.blit(seringue.photo, (seringue.x, seringue.y))
		pygame.display.flip()