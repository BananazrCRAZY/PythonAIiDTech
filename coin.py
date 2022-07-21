import pygame

class Coin(pygame.sprite.Sprite):
    SIZE = (30, 30)
    IMAGE = pygame.image.load('resources/treasure.png')
    POSITION = (300, 250)
    SCREEN_DIM = 600, 600

    def __init__(self, position: tuple):
        super().__init__()
        self.image = Coin.IMAGE
        self.rect = pygame.Rect((0, 0), Coin.SIZE)
        self.rect.center = position