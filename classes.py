"""Classes du jeu du Labyrinthe de MacGyver"""

import pygame
from pygame.locals import * 
from constantes import *

class Map:
	def __init__(self, fichier_lab):
		self.fichier_lab = fichier_lab
		self.structure = 0

	def generer(self):
		"Générer la map en fonction du fichier"
		with open(labyrinth.txt, "r") as fichier_lab