import pygame, sys, random
from frog import Frog
from street import Street
from rivers import River

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 500
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('Frogger')
CLOCK = pygame.time.Clock()
FPS = 30

score = 0
current_best = 0
high_score = 0

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (24, 66, 23)
YELLOW = (162, 170, 56)
BROWN = (118, 92, 72)
GRAY = (72, 72, 72)
LIGHT_GRAY = (137, 137, 137)
BLUE = (0, 77, 145)

FONT = pygame.font.Font('resources/joystix monospace.ttf', 20)

streets = []
number_of_buses = 3
street_height = 400
for _ in range(2):
      streets.append(Street(street_height, 'Left', random.randint(1, number_of_buses)))
      streets.append(Street(street_height - 40, 'Right', random.randint(1, number_of_buses)))
      street_height -= 80

riverss = []
number_of_logs = 4
river_height = 40
for _ in range(2):
      riverss.append(River(river_height, 'Left', random.randint(1, number_of_logs)))
      riverss.append(River(river_height + 40, 'Right', random.randint(1, number_of_logs)))
      river_height += 80

frog = Frog()

while frog.lives > 0:
    CLOCK.tick(FPS)
    SCREEN.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                # Add the correct frog movement function here
                frog.move_up()
            if event.key == pygame.K_a:  # A
                # Add the correct frog movement function here
                frog.move_left()
            if event.key == pygame.K_s:  # S
                # Add the correct frog movement function here
                frog.move_down()
            if event.key == pygame.K_d:  # D
                # Add the correct frog movement function here
                frog.move_right()

    for street in streets:
        SCREEN.fill(LIGHT_GRAY, street.rect)
        for bus in street.buses:
            SCREEN.blit(bus.image, bus.rect)
            bus.move()
            if frog.rect.colliderect(bus.rect):
                frog.reset_position()

        # Act on rivers and logs
        frog_on_log = False  # new
        for rivers in riverss:
            # Draw River
            SCREEN.fill(BLUE, rivers.rect)

            # Log
            for log in rivers.logs:
                SCREEN.blit(log.image, log.rect)
                log.move()
                if frog.rect.colliderect(log.rect):
                    frog.move_on_log(log)
                    frog_on_log = True  # new

            for ufo in rivers.ufos:
                SCREEN.blit(ufo.image, ufo.rect)
                ufo.move()
                if frog.rect.colliderect(ufo.rect):
                    frog.reset_position()
                    frog.reset_position()

            # Collided with River and not a Log - new
            if not frog_on_log and frog.rect.colliderect(rivers.rect):
                frog.reset_position()

    if 475 - frog.rect.top > current_best:
        current_best = 475 - frog.rect.top
    if score + current_best >= high_score:
        high_score = score + current_best
    if frog.rect.top <= 39:
        frog.reset_position()
        frog.lives += 2
        score += 1000 + current_best
        current_best = 0
        print("Score: " + str(score + current_best))
        print("High Score: " + str(high_score))
        print("Lives: " + str(frog.lives))

    SCREEN.blit(frog.image, frog.rect)

    pygame.display.flip()