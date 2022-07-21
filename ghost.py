import pygame, random
import self


class Ghost(pygame.sprite.Sprite):
    SIZE = (20, 20)
    IMAGE = pygame.image.load('resources/ghost.png')
    POSITION = (300, 250)
    SCREEN_DIM = 600, 600
    MOVE_DIST = 0
    DEAD = False
    CIRCLE = pygame.Rect((0, 0), (120, 120))
    CIRCLE1 = pygame.Rect((0, 0), (100, 100))
    CIRCLE2 = pygame.Rect((0, 0), (80, 80))
    CIRCLE3 = pygame.Rect((0, 0), (60, 60))
    CIRCLE4 = pygame.Rect((0, 0), (40, 40))

    def __init__(self, position: tuple, MOVE_DIST: int, stealth: int):
        super().__init__()
        self.image = Ghost.IMAGE
        self.rect = pygame.Rect((0, 0), Ghost.SIZE)
        self.rect.center = position
        self.MOVE_DIST = MOVE_DIST
        self.CIRCLE = pygame.Rect(self.rect.center, (stealth, stealth))
        self.CIRCLE1 = pygame.Rect(self.rect.center, (stealth - 20, stealth - 20))
        self.CIRCLE2 = pygame.Rect(self.rect.center, (stealth - 40, stealth - 40))
        self.CIRCLE3 = pygame.Rect(self.rect.center, (stealth - 60, stealth - 60))
        self.CIRCLE4 = pygame.Rect(self.rect.center, (stealth - 80, stealth - 80))

    def move(self):
        num = random.randint(0, 3)
        if num == 0:
            if not (self.rect.centerx - self.MOVE_DIST) < 0:
                self.rect.centerx -= self.MOVE_DIST
        elif num == 1:
            if not (self.rect.centerx + self.MOVE_DIST) > 580:
                self.rect.centerx += self.MOVE_DIST
        elif num == 2:
            if not (self.rect.centery + self.MOVE_DIST) > 580:
                self.rect.centery += self.MOVE_DIST
        else:
            if not (self.rect.centery - self.MOVE_DIST) < 0:
                self.rect.centery -= self.MOVE_DIST
