import pygame, random

class Ghost(pygame.sprite.Sprite):
    SIZE = (20, 20)
    IMAGE = pygame.image.load('resources/ghost.png')
    POSITION = (300, 250)
    SCREEN_DIM = 600, 600
    MOVE_DIST = 0

    def __init__(self, position: tuple, MOVE_DIST: int):
        super().__init__()
        self.image = Ghost.IMAGE
        self.rect = pygame.Rect((0, 0), Ghost.SIZE)
        self.rect.center = position
        self.MOVE_DIST = MOVE_DIST

    def move(self):
        num = random.randint(0, 4)
        if num == 0:
            self.rect.centerx -= Ghost.MOVE_DIST
            if Ghost.rect.left <= 0:
