import pygame

class UFO(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/ufo.png')
    STARTING_POSITION = (300, 90)
    SIZE = (60, 30)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 4

    # Creates a Log object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = UFO.IMAGE
        # Log Information
        self.rect = pygame.Rect((0, 0), UFO.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Log is going left
        if self.direction == 'Left':
            self.rect.centerx -= UFO.MOVE_DIST
            # Log has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = UFO.SCREEN_DIM[0] + UFO.SIZE[0] / 2
        # Log is going right
        else:
            self.rect.centerx += UFO.MOVE_DIST
            # Log has moved off the screen
            if self.rect.left >= UFO.SCREEN_DIM[0]:
                self.rect.centerx = -UFO.SIZE[0] / 2