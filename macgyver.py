# -*- coding: Utf-8 -*
""" Main file to play the MacGyver maze game"""

import pygame

import classes
import constants

pygame.init()

#Open maze screen and display the settings
SCREEN = pygame.display.set_mode((constants.SCREEN_SIDE, constants.SCREEN_SIDE + constants.SPACE_LINE))

#Icon
ICON = pygame.image.load(constants.MACGYVER_IMG)
pygame.display.set_icon(ICON)

#Title
pygame.display.set_caption(constants.TITLE)

#Background
GREY = [206, 206, 206]
SCREEN.fill(GREY)

#Create map
MAP = classes.Map(constants.MAZE_FILE)
MAP.create()
MAP.afficher(SCREEN)

#Create MacGyver
MACGYVER = classes.MacGyver(constants.MACGYVER_IMG, constants.MACGYVER_IMG, constants.MACGYVER_IMG, constants.MACGYVER_IMG, MAP)

#Create objects
SYRINGE = classes.Object(constants.SYRINGE_IMG, MAP)
ETHER = classes.Object(constants.ETHER_IMG, MAP)
NEEDLE = classes.Object(constants.NEEDLE_IMG, MAP)

#Game loop
CONTINUE_GAME = 1
pygame.key.set_repeat(400, 30)
while CONTINUE_GAME:
    MACGYVER.display_counter(SCREEN)
    for event in pygame.event.get():

        #Quit game
        if event.type == pygame.QUIT:
            CONTINUE_GAME = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                CONTINUE_GAME = 0
            #keydown to move MacGyver
            elif event.key == pygame.K_RIGHT:
                MACGYVER.deplacer("right")
            elif event.key == pygame.K_LEFT:
                MACGYVER.deplacer("left")
            elif event.key == pygame.K_UP:
                MACGYVER.deplacer("up")
            elif event.key == pygame.K_DOWN:
                MACGYVER.deplacer("down")

    #Display map, MacGyver and objects
    MAP.afficher(SCREEN)
    SCREEN.blit(MACGYVER.direction, (MACGYVER.x, MACGYVER.y))
    SYRINGE.display(SCREEN)
    NEEDLE.display(SCREEN)
    ETHER.display(SCREEN)

    #Pick up the objects
    if MACGYVER.x == SYRINGE.x and MACGYVER.y == SYRINGE.y:
        SYRINGE.life -= 1
        MACGYVER.counter()
    if MACGYVER.x == NEEDLE.x and MACGYVER.y == NEEDLE.y:
        NEEDLE.life -= 1
        MACGYVER.counter()
    if MACGYVER.x == ETHER.x and MACGYVER.y == ETHER.y:
        ETHER.life -= 1
        MACGYVER.counter()

    #Victory and defeat
    VICTORY = pygame.font.SysFont("monospace", 30)
    TEXT_VICTORY = VICTORY.render("You win!", 1, (0, 128, 0), (206, 206, 206))
    LOOSE = pygame.font.SysFont("monospace", 30)
    TEXT_LOOSE = LOOSE.render("You loose!", 1, (0, 128, 0), (206, 206, 206))
    if MAP.structure[MACGYVER.sprite_y][MACGYVER.sprite_x] == "a" and MACGYVER.mg_counter >= 3:
        SCREEN.blit(TEXT_VICTORY, (145, 200))
        PROCEED = 0
        CONTINUE_GAME = 0
    if MAP.structure[MACGYVER.sprite_y][MACGYVER.sprite_x] == "a" and MACGYVER.mg_counter < 3:
        SCREEN.blit(TEXT_LOOSE, (140, 200))
        PROCEED = 0
        CONTINUE_GAME = 0

    pygame.display.flip()