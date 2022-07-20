import pygame, sys
from log import Log

class Frog(pygame.sprite.Sprite):
    STARTING_POSITION = (300, 490)
    SIZE = (20, 20)
    IMAGE = pygame.image.load('resources/frog.png')
    MOVE_DIST = 40
    SCREEN_DIM = 600, 500

    def __init__(self):
        super().__init__()
        self.image = Frog.IMAGE

        self.lives = 3
        self.rect = pygame.Rect((0, 0), Frog.SIZE)
        self.rect.center = Frog.STARTING_POSITION

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Frog.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= 480:
            self.rect.centery += Frog.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Frog.MOVE_DIST

    def move_right(self):
        if self.rect.right <= 580:
            self.rect.centerx += Frog.MOVE_DIST

    def reset_position(self):
        self.rect.center = Frog.STARTING_POSITION
        self.lives -= 1
        print("Lives Left: " + str(self.lives))

    def move_on_log(self, log: Log):
        # Log moving right
        if log.direction == 'Right':
            self.rect.centerx += Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.left >= Log.SCREEN_DIM[0]:
                diff = log.rect.right - self.rect.centerx
                self.rect.centerx = -diff
        # Log moving left
        else:
            self.rect.centerx -= Log.MOVE_DIST
            # Frog has moved off screen
            if self.rect.right <= 0:
                diff = abs(log.rect.left - self.rect.centerx)
                self.rect.centerx = Frog.SCREEN_DIM[0] + diff