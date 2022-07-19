import pygame
pygame.init()
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Frogger')
CLOCK = pygame.time.Clock()
FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 66, 23)
YELLOW = (162, 170, 56)
BROWN = (118, 92, 72)
GRAY = (72, 72, 72)
BLUE = (0, 77, 145)

while True:
    CLOCK.tick(FPS)
    SCREEN.fill(BLACK)
    pygame.display.flip()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        break
