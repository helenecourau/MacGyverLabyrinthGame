"""Classes du jeu du Labyrinthe de MacGyver"""

import pygame
from pygame.locals import * 
import random

from constantes import *

class Map:
	"""Classe pour générer la map"""
	def __init__(self, fichier_lab):
		self.fichier_lab = fichier_lab
		self.structure = 0

	def generer(self):
		"Générer la map en fonction du fichier"
		with open(self.fichier_lab, "r") as fichier_lab:
			structure_lab = []
			for ligne in fichier_lab:
				ligne_lab = []
				for sprite in ligne:
					if sprite != "\n":
						ligne_lab.append(sprite)
				structure_lab.append(ligne_lab)
			self.structure = structure_lab

	def afficher(self, fenetre):
		"Afficher la map avec la liste renvoyée par generer()"
		mur = pygame.image.load(image_mur).convert()
		fond = pygame.image.load(image_fond).convert()
		gardien = pygame.image.load(image_gardien).convert()

		num_ligne = 0
		for ligne in self.structure:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == "m":
					fenetre.blit(mur, (x,y))
				elif sprite == "a" :
					fenetre.blit(gardien, (x,y))
				elif sprite == "o" or "d":
					fenetre.blit(fond, (x,y))
				num_case += 1
			num_ligne += 1

class MacGyver:
	"""Créer le personnage et le faire se déplacer"""
	
	def __init__(self, droite, gauche, haut, bas, lab):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		self.direction = self.droite
		self.lab = lab

	def deplacer(self, direction):
		
		#droite
		if direction == "droite":
			if self.case_x < (nombre_sprite_cote - 1):
				if self.lab.structure[self.case_y][self.case_x+1] != "m":
					self.case_x += 1
					self.x = self.case_x * taille_sprite
			self.direction = self.droite
		
		#gauche
		if direction == "gauche":
			if self.case_x > 0:
				if self.lab.structure[self.case_y][self.case_x-1] != "m":
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#haut
		if direction == "haut":
			if self.case_y > 0:
				if self.lab.structure [self.case_y-1][self.case_x] != "m":
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		#bas
		if direction == "bas":
			if self.case_y < (nombre_sprite_cote - 1):
				if self.lab.structure[self.case_y+1][self.case_x] != "m":
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas

class Objet:
	"""Créer les objets et les faire apparaître au hasard"""

	def __init__(self, photo, lab):
		self.photo = pygame.image.load(photo).convert_alpha()
		self.x = 0
		self.y = 0
		self.case_x = 0
		self.case_y = 0
		self.lab = lab
		if self.lab.structure[self.case_y][self.case_x] != "m":
			self.case_x = random.randrange(0, cote_fenetre, taille_sprite)
			self.case_y = random.randrange(0, cote_fenetre, taille_sprite)