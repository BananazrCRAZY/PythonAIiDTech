import pygame

class Log(pygame.sprite.Sprite):
    # Define constant values
    IMAGE = pygame.image.load('resources/log.png')
    STARTING_POSITION = (300, 150)
    SIZE = (60, 40)
    SCREEN_DIM = 600, 500
    MOVE_DIST = 1

    # Creates a Log object
    def __init__(self, starting_position: tuple, direction: str):
        # Sprite Information
        super().__init__()
        self.image = Log.IMAGE
        # Log Information
        self.rect = pygame.Rect((0, 0), Log.SIZE)
        self.rect.center = starting_position
        self.direction = direction

    def move(self):
        # Log is going left
        if self.direction == 'Left':
            self.rect.centerx -= Log.MOVE_DIST
            # Log has moved off the screen
            if self.rect.right <= 0:
                self.rect.centerx = Log.SCREEN_DIM[0] + Log.SIZE[0] / 2
        # Log is going right
        else:
            self.rect.centerx += Log.MOVE_DIST
            # Log has moved off the screen
            if self.rect.left >= Log.SCREEN_DIM[0]:
                self.rect.centerx = -Log.SIZE[0] / 2