"""Classes du jeu du Labyrinthe de MacGyver"""

import pygame
from pygame.locals import * 
from constantes import *

class Map:
	def __init__(self, fichier_lab):
		self.fichier_lab = fichier_lab
		self.structure = 0