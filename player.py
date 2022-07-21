import pygame

class Player(pygame.sprite.Sprite):
    STARTING_POSITION = (300, 300)
    SIZE = (20, 20)
    IMAGE = pygame.image.load('resources/player.png')
    MOVE_DIST = 20
    SCREEN_DIM = 600, 600
    DEAD = False

    def __init__(self):
        super().__init__()
        self.image = Player.IMAGE

        self.rect = pygame.Rect((0, 0), Player.SIZE)
        self.rect.center = Player.STARTING_POSITION

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Player.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= 580:
            self.rect.centery += Player.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Player.MOVE_DIST

    def move_right(self):
        if self.rect.right <= 580:
            self.rect.centerx += Player.MOVE_DIST