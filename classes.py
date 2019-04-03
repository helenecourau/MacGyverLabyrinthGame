"""MacGyver maze game classes"""

import random
import pygame

import constants


class Map:
    """Map generation"""
    
    def __init__(self, maze_file):
        self.maze_file = maze_file
        self.structure = []

    def create(self):
        """Create the map with the .txt file"""
        with open(self.maze_file, "r") as maze_file:
            for line in maze_file:
                line_maze = []
                for sprite in line:
                    if sprite != "\n":
                        line_maze.append(sprite)
                self.structure.append(line_maze)

    def display_map(self, screen):
        """Display map with the list return by create()"""
        path = pygame.image.load(constants.PATH_IMG).convert()
        guardian = pygame.image.load(constants.GUARDIAN_IMG).convert()
        wall = pygame.image.load(constants.WALL_IMG).convert()

        num_line = 0
        for line in self.structure:
            num_sprite = 0
            for sprite in line:
                x = num_sprite * constants.SPRITE_SIZE
                y = num_line * constants.SPRITE_SIZE + constants.SPACE_LINE
                if sprite == "w":
                    screen.blit(wall, (x, y))
                elif sprite == "e":
                    screen.blit(guardian, (x, y))
                elif sprite == "o" or "s":
                    screen.blit(path, (x, y))
                num_sprite += 1
            num_line += 1


class MacGyver:
    """Create MacGyver, move it and pickup the objects"""

    def __init__(self, image, maze):
        self.image = pygame.image.load(image).convert_alpha()
        self.sprite_x = 0
        self.sprite_y = 0
        self.x = self.sprite_x * constants.SPRITE_SIZE
        self.y = self.sprite_y * constants.SPRITE_SIZE + constants.SPACE_LINE
        self.maze = maze
        self.mg_counter = 0

    def move(self, direction):
        """Move MacGyver with the sprite numbers"""

        # right
        if direction == "right":
            if self.sprite_x < (constants.MAX_SPRITES_SIZE - 1):
                if self.maze.structure[self.sprite_y][self.sprite_x+1] != "w":
                    self.sprite_x += 1
                    self.x = self.sprite_x * constants.SPRITE_SIZE

        # left
        if direction == "left":
            if self.sprite_x > 0:
                if self.maze.structure[self.sprite_y][self.sprite_x-1] != "w":
                    self.sprite_x -= 1
                    self.x = self.sprite_x * constants.SPRITE_SIZE

        # up
        if direction == "up":
            if self.sprite_y > 0:
                if self.maze.structure[self.sprite_y-1][self.sprite_x] != "w":
                    self.sprite_y -= 1
                    self.y = self.sprite_y *\
                        constants.SPRITE_SIZE + constants.SPACE_LINE

        # down
        if direction == "down":
            if self.sprite_y < (constants.MAX_SPRITES_SIZE - 1):
                if self.maze.structure[self.sprite_y+1][self.sprite_x] != "w":
                    self.sprite_y += 1
                    self.y = self.sprite_y *\
                        constants.SPRITE_SIZE + constants.SPACE_LINE

    def counter(self):
        """Count the objects picked up by MacGyver
        when it is on the right position"""
        if self.maze.structure[self.sprite_y][self.sprite_x] == "b":
            self.maze.structure[self.sprite_y][self.sprite_x] = "o"
            self.mg_counter = self.mg_counter + 1

    def display_counter(self, SCREEN):
        """Display the counter with a text way and not an image"""
        counter = pygame.font.SysFont("monospace", 15, 0)
        text_counter = counter.render(
            "Objects : " + str(self.mg_counter), 0, (0, 128, 0))
        SCREEN.blit(text_counter, (5, 5))


class Object:
    """Create objects on random location"""
   
    def __init__(self, image, maze):
        self.image = pygame.image.load(image).convert_alpha()
        self.maze = maze
        self.sprite_x, self.sprite_y = self.generate()
        self.x = self.sprite_x * constants.SPRITE_SIZE
        self.y = self.sprite_y * constants.SPRITE_SIZE + constants.SPACE_LINE
        self.life = 1  # to erase objects image and location

    def generate(self):
        """Generate objects with the .txt file"""
        test = 0
        while test < 1:
            self.sprite_y = random.randrange(constants.MAX_SPRITES_SIZE)
            self.sprite_x = random.randrange(constants.MAX_SPRITES_SIZE)
            # make sure that the objets are where MacGyver can go
            if self.maze.structure[self.sprite_y][self.sprite_x] == "o":
                # make sure that two objects can't be on the same sprite
                self.maze.structure[self.sprite_y][self.sprite_x] = "b"
                test += 1
        return self.sprite_x, self.sprite_y

    def display(self, SCREEN):
        """Display the objects on the map"""
        if self.life > 0:  # erase object's images
            SCREEN.blit(self.image, (self.x, self.y))
        # when they have been picked up,
        # the objects location is where MacGyver can't go
        if self.life < 0:
            self.x = 0
            self.y = 0
