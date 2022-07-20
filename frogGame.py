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
MENU_BIG = pygame.font.Font('resources/joystix monospace.ttf', 60)
MENU_MED = pygame.font.Font('resources/joystix monospace.ttf', 25)
MENU_SMALL = pygame.font.Font('resources/joystix monospace.ttf', 15)
MENU_IMAGE = pygame.image.load('resources/menu.png')
START_MENU = True
END_MENU = False

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

while True:
    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(GREEN)

        name = MENU_BIG.render('FROGGER', True, WHITE)
        instructions = MENU_SMALL.render('PRESS SPACE TO START', True, WHITE)
        SCREEN.blit(name, (130, 130))
        SCREEN.blit(instructions, (180, 210))
        SCREEN.blit(MENU_IMAGE, (145, 260))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False
        pygame.display.update()

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

            # Collided with River and not a Log - new
            if not frog_on_log and frog.rect.colliderect(rivers.rect):
                frog.reset_position()

    if 475 - frog.rect.top > current_best:
        current_best = 475 - frog.rect.top
    if score + current_best >= high_score:
        high_score = score + current_best
    if frog.rect.top <= 39:
        frog.reset_position()
        FPS += 10
        if frog.lives < 3:
            frog.lives += 2
        score += 1000 + current_best
        current_best = 0

    score_text = FONT.render("Score: " + str(score + current_best), True, WHITE)
    high_score_text = FONT.render("High Score: " + str(high_score), True, WHITE)
    lives_text = FONT.render("Lives: " + str(frog.lives), True, WHITE)

    SCREEN.blit(score_text, (5, 0))
    SCREEN.blit(high_score_text, (5, 20))
    SCREEN.blit(lives_text, (5, 40))

    SCREEN.blit(frog.image, frog.rect)
    pygame.display.flip()

    if frog.lives <= 0:
        END_MENU = True

    while END_MENU:
        CLOCK.tick(15)
        SCREEN.fill(GREEN)

        thx = MENU_MED.render('Thanks for Playing!', True, WHITE)
        scores = MENU_MED.render('Your Final Score: %d' % (score + current_best), True, WHITE)
        instructions = MENU_SMALL.render('Press \'Space\' To Play Again', True, WHITE)
        SCREEN.blit(thx, (85, 120))
        SCREEN.blit(scores, (70, 180))
        SCREEN.blit(instructions, (130, 240))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_best = 0
                    score = 0
                    frog.lives = 3
                    FPS = 30
                    END_MENU = False
        pygame.display.update()