import pygame

class Cursor(pygame.sprite.Sprite):
    SIZE = (30, 30)
    IMAGE = pygame.image.load('resources/treasure.png')
    SCREEN_DIM = 600, 600
    MOVE_DIST_X = 300
    MOVE_DIST_Y = 120


    def __init__(self):
        super().__init__()
        self.image = Cursor.IMAGE
        self.rect = pygame.Rect((150, 400), Cursor.SIZE)

    def move_up(self):
        if self.rect.top > 400:
            self.rect.centery -= Cursor.MOVE_DIST_Y

    def move_down(self):
        if self.rect.bottom < 520:
            self.rect.centery += Cursor.MOVE_DIST_Y

    def move_left(self):
        if self.rect.left > 150:
            self.rect.centerx -= Cursor.MOVE_DIST_X

    def move_right(self):
        if self.rect.right < 450:
            self.rect.centerx += Cursor.MOVE_DIST_X