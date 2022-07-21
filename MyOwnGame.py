import time

import pygame, sys, random
from Bots import Bots
from player import Player
from ghost import Ghost
from coin import Coin

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
SCREEN_DIM = WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode(SCREEN_DIM)
pygame.display.set_caption('YOUR ADVENTURE')
CLOCK = pygame.time.Clock()
FPS = 120

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
MENU_IMAGE = pygame.image.load('resources/menuImage.png')
DARK = pygame.image.load('resources/dark.png')
DARK1 = pygame.image.load('resources/dark1.png')
DARK2 = pygame.image.load('resources/dark2.png')
DARK3 = pygame.image.load('resources/dark3.png')
DARK4 = pygame.image.load('resources/dark4.png')
DARK5 = pygame.image.load('resources/dark5.png')
END_SCREEN = pygame.image.load('resources/endScreen.png')

START_MENU = True
INFO_REQ = False
BATTLE = False
GAMEOVER = False
need_spawn = True
WIN = False

NAME = ""
player = Player()

ghosts = []

while True:
    while START_MENU:
        CLOCK.tick(15)
        SCREEN.fill(BLACK)

        name = MENU_BIG.render('DUNGEON', True, WHITE)
        instructions = MENU_SMALL.render('PRESS SPACE TO START', True, WHITE)
        SCREEN.blit(name, (129, 80))
        SCREEN.blit(instructions, (180, 160))
        SCREEN.blit(MENU_IMAGE, (145, 220))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    START_MENU = False
                    INFO_REQ = True
        pygame.display.update()

    while INFO_REQ:
        CLOCK.tick(15)
        SCREEN.fill(BLACK)
        instructions = MENU_SMALL.render('THIS GAME USES THE CONSOLE', True, WHITE)
        SCREEN.blit(instructions, (140, 160))
        SCREEN.blit(player.image, player.rect)
        pygame.display.update()

        NAME = input("WHAT IS YOUR NAME?\n")
        NAME = NAME.upper()
        fighting_player = Bots(NAME, 10)
        pygame.display.set_caption(NAME + "'S ADVENTURE")
        INFO_REQ = False

    # Start of Game
    CLOCK.tick(FPS)
    SCREEN.fill(GRAY)

    # One time thing
    while need_spawn:
        for num in range(0, 20):
            ghosts.append(Ghost((random.randint(0, 600), random.randint(0, 600)), random.randint(0, 1), 120))
        coin = Coin((random.randint(1, 569), random.randint(1, 569)))
        need_spawn = False

    SCREEN.blit(coin.image, coin.rect)

    for ghost in ghosts:
        ghost.move()
        if player.rect.colliderect(ghost.rect):
            SCREEN.blit(DARK5, (0, 0))
            SCREEN.blit(ghost.image, ghost.rect)
            pygame.display.update()

            BATTLE = True
            print("YOU'VE ENCOUNTERED A GHOST")
            time.sleep(2)
            while BATTLE:
                CLOCK.tick(FPS)
                SCREEN.fill(BLACK)
                pygame.display.update()

                fighting_player = Bots(NAME, 10)
                if ghost.DEAD or player.DEAD:
                    BATTLE = False

        elif player.rect.colliderect(ghost.CIRCLE4):
            SCREEN.blit(DARK4, (0, 0))
            pygame.display.update()
        elif player.rect.colliderect(ghost.CIRCLE3):
            SCREEN.blit(DARK3, (0, 0))
            pygame.display.update()
        elif player.rect.colliderect(ghost.CIRCLE2):
            SCREEN.blit(DARK2, (0, 0))
            pygame.display.update()
        elif player.rect.colliderect(ghost.CIRCLE1):
            SCREEN.blit(DARK1, (0, 0))
            pygame.display.update()
        elif player.rect.colliderect(ghost.CIRCLE):
            SCREEN.blit(DARK, (0, 0))
            pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # W
                # Add the correct frog movement function here
                player.move_up()
            if event.key == pygame.K_a:  # A
                # Add the correct frog movement function here
                player.move_left()
            if event.key == pygame.K_s:  # S
                # Add the correct frog movement function here
                player.move_down()
            if event.key == pygame.K_d:  # D
                # Add the correct frog movement function here
                player.move_right()

    SCREEN.blit(player.image, player.rect)
    pygame.display.flip()

    if player.rect.colliderect(coin.rect):
        GAMEOVER = True
        WIN = True

    while GAMEOVER:
        CLOCK.tick(15)
        SCREEN.fill(BLACK)

        if WIN:
            name = MENU_BIG.render('YOU WIN', True, WHITE)
            SCREEN.blit(name, (129, 80))
            SCREEN.blit(END_SCREEN, (170, 220))
        else:
            name = MENU_BIG.render('YOU LOSE', True, WHITE)
            SCREEN.blit(name, (110, 80))
            SCREEN.blit(MENU_IMAGE, (145, 220))

        instructions = MENU_SMALL.render('PRESS SPACE PLAY AGAIN', True, WHITE)
        SCREEN.blit(instructions, (180, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAMEOVER = False
                    WIN = False
                    need_spawn = True
        pygame.display.update()