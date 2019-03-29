# -*- coding: Utf-8 -*
""" Main file to play the MacGyver maze game"""

import pygame

import classes
import constants

pygame.init()

# Open maze screen and display the settings
SCREEN = pygame.display.set_mode((
    constants.SCREEN_SIDE, constants.SCREEN_SIDE + constants.SPACE_LINE))

# Icon
ICON = pygame.image.load(constants.MACGYVER_IMG)
pygame.display.set_icon(ICON)

# Title
pygame.display.set_caption(constants.TITLE)

# Background
GREY = [206, 206, 206]
SCREEN.fill(GREY)

# MAIN LOOP
CONTINUE_PROGRAM = 1
while CONTINUE_PROGRAM:
    FIRST_SCREEN_IMG = pygame.image.load(constants.FIRST_SCREEN).convert()
    SCREEN.blit(FIRST_SCREEN_IMG, (0, 30))
    pygame.display.flip()
    CONTINUE_GAME = 1
    FIRST_SCREEN = 1

    while FIRST_SCREEN:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type\
                    == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                FIRST_SCREEN = 0
                CONTINUE_PROGRAM = 0
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    # Create map
                    MAP = classes.Map(constants.MAZE_FILE)
                    MAP.create()
                    MAP.display_map(SCREEN)

                    # Create MacGyver
                    MACGYVER = classes.MacGyver(constants.MACGYVER_IMG, MAP)

                    # Create objects
                    SYRINGE = classes.Object(constants.SYRINGE_IMG, MAP)
                    ETHER = classes.Object(constants.ETHER_IMG, MAP)
                    NEEDLE = classes.Object(constants.NEEDLE_IMG, MAP)

                    # Game loop
                    pygame.key.set_repeat(400, 30)
                    while CONTINUE_GAME:
                        MACGYVER.display_counter(SCREEN)
                        for event in pygame.event.get():

                            # Quit game
                            if event.type == pygame.QUIT:
                                CONTINUE_GAME = 0
                                FIRST_SCREEN = 0
                                CONTINUE_PROGRAM = 0
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    CONTINUE_GAME = 0
                                    FIRST_SCREEN = 0
                                # keydown to move MacGyver
                                elif event.key == pygame.K_RIGHT:
                                    MACGYVER.move("right")
                                elif event.key == pygame.K_LEFT:
                                    MACGYVER.move("left")
                                elif event.key == pygame.K_UP:
                                    MACGYVER.move("up")
                                elif event.key == pygame.K_DOWN:
                                    MACGYVER.move("down")

                        # Display map, MacGyver and objects
                        MAP.display_map(SCREEN)
                        SCREEN.blit(
                            MACGYVER.image, (MACGYVER.x, MACGYVER.y))
                        SYRINGE.display(SCREEN)
                        NEEDLE.display(SCREEN)
                        ETHER.display(SCREEN)

                        # Pick up the objects
                        if MACGYVER.x == SYRINGE.x and MACGYVER.y == SYRINGE.y:
                            SYRINGE.life -= 1
                            SCREEN.fill(pygame.Color("GREY"), (0, 0, 450, 30))
                            MACGYVER.counter()
                        if MACGYVER.x == NEEDLE.x and MACGYVER.y == NEEDLE.y:
                            NEEDLE.life -= 1
                            SCREEN.fill(pygame.Color("GREY"), (0, 0, 450, 30))
                            MACGYVER.counter()
                        if MACGYVER.x == ETHER.x and MACGYVER.y == ETHER.y:
                            ETHER.life -= 1
                            SCREEN.fill(pygame.Color("GREY"), (0, 0, 450, 30))
                            MACGYVER.counter()

                        # Victory and defeat
                        VICTORY = pygame.font.SysFont(
                            "monospace", 25, bold=True)
                        TEXT_VICTORY = VICTORY.render(
                            "You win!", 1, (0, 128, 0), (206, 206, 206))
                        LOOSE = pygame.font.SysFont("monospace", 25, bold=True)
                        TEXT_LOOSE = LOOSE.render(
                            "You loose!", 1, (255, 64, 64), (206, 206, 206))
                        AGAIN = pygame.font.SysFont("monospace", 25)
                        TEXT_AGAIN = VICTORY.render(
                            "Press escape to play again", 0, (
                                19, 14, 10), (206, 206, 206))
                        if MAP.structure[MACGYVER.sprite_y]\
                                [MACGYVER.sprite_x] == "a":
                            SCREEN.blit(TEXT_AGAIN, (30, 250))
                            if MACGYVER.mg_counter >= 3:
                                SCREEN.blit(TEXT_VICTORY, (145, 200))
                            if MACGYVER.mg_counter < 3:
                                SCREEN.blit(TEXT_LOOSE, (145, 200))
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                CONTINUE_GAME = 0
                                FIRST_SCREEN = 0
                                SCREEN.fill(pygame.Color("GREY"),
                                            (0, 0, 450, 30))

                        pygame.display.flip()                        