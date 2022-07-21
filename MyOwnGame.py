import time

import pygame, sys, random
from Bots import Bots
from player import Player
from ghost import Ghost
from coin import Coin
from cursor import Cursor

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
FIGHT_MENU = pygame.image.load('resources/fightMenu.png')
CHECK_CONSOLE = pygame.image.load('resources/checkConsole.png')
END_SCREEN = pygame.image.load('resources/endScreen.png')

START_MENU = True
INFO_REQ = False
BATTLE = False
GAMEOVER = False
need_spawn = True
WIN = False
YOUR_TURN = True
SCORE = 0

NAME = ""
player = Player()
cursor = Cursor()

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
        instructions4 = MENU_SMALL.render('WARNING: THERE ARE FLASHING IMAGES', True, WHITE)
        instructions6 = MENU_SMALL.render('IN THIS GAME', True, WHITE)
        instructions = MENU_SMALL.render('THIS GAME USES THE CONSOLE', True, WHITE)
        instructions1 = MENU_SMALL.render('INPUTTING SOMETHING OTHER THAN A NUMBER WHEN', True, WHITE)
        instructions2 = MENU_SMALL.render('ASKED WILL RESULT IN THE GAME CRASHING AND', True, WHITE)
        instructions7 = MENU_SMALL.render('ALL PROGRESS LOST', True, WHITE)
        instructions3 = MENU_SMALL.render('THERE IS NO BACK IN THIS GAME', True, WHITE)
        instructions5 = MENU_SMALL.render('PLEASE CHECK THE CONSOLE\n', True, WHITE)
        SCREEN.blit(instructions4, (50, 120))
        SCREEN.blit(instructions6, (50, 160))
        SCREEN.blit(instructions, (50, 240))
        SCREEN.blit(instructions1, (50, 280))
        SCREEN.blit(instructions2, (50, 320))
        SCREEN.blit(instructions7, (50, 360))
        SCREEN.blit(instructions3, (50, 440))
        SCREEN.blit(instructions5, (50, 480))
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
            ghosts.append(Ghost((random.randint(0, 600), random.randint(0, 600)), random.randint(0, 1), 120,
                                random.randint(50, 100), random.randint(8, 11), random.randint(8, 11),
                                random.randint(8, 11)))
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
            time.sleep(1)
            while BATTLE:
                CLOCK.tick(FPS)
                fighting_player = Bots(NAME, 10)

                SCREEN.fill(BLACK)
                SCREEN.blit(FIGHT_MENU, (0, 0))
                SCREEN.blit(cursor.image, cursor.rect)
                pygame.display.flip()

                if YOUR_TURN:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_w:  # W
                                cursor.move_up()
                            if event.key == pygame.K_a:  # A
                                cursor.move_left()
                            if event.key == pygame.K_s:  # S
                                cursor.move_down()
                            if event.key == pygame.K_d:  # D
                                cursor.move_right()
                            if event.key == pygame.K_SPACE:
                                # attack
                                if cursor.rect.center == (165, 415):
                                    SCREEN.blit(CHECK_CONSOLE, (0, 0))
                                    pygame.display.update()
                                    input("SELECT AN ATTACK:\n")
                                    YOUR_TURN = False
                                # heal
                                elif cursor.rect.center == (465, 415):
                                    print("YOU HEALED")
                                    player.heal()
                                    YOUR_TURN = False
                                # stats
                                elif cursor.rect.center == (165, 535):
                                    SCREEN.blit(CHECK_CONSOLE, (0, 0))
                                    pygame.display.update()
                                    buff_or_nerf = int(input("WOULD YOU LIKE TO BUFF OR NERF A STAT:\n"
                                                             "1. BUFF\n2. NERF\n"))
                                    stat = int(input("SELECT A STAT:\n1. ATTACK\n2. DEFENCE\n3. SPEED\n4. AFFECT\n"
                                                    "5. CRIT CHANCE\n6. CRIT MULTIPLIER\n"))
                                    YOUR_TURN = False
                                    #if buff_or_nerf == 1:
                                # info
                                elif cursor.rect.center == (465, 535):
                                    SCREEN.blit(CHECK_CONSOLE, (0, 0))
                                    pygame.display.update()
                                    info = int(input("WOULD YOU LIKE TO SEE THE STATS OR INSTRUCTIONS:\n"
                                                "1. STATS\n2. INSTRUCTIONS\n"))
                                    if info == 2:
                                        input("GENERAL BATTLE INFO:\nWHEN YOU RUN INTO AN ENEMY A BATTLE STARTS\n"
                                              "WHEN OPPONENTS ARE DEFEATED THEY ADD TO YOUR SCORE\n"
                                              "THE HARDER THE ENEMY THE MORE POINTS YOU WILL GET\n"
                                              "HP WILL CARRY OVER FROM BATTLE TO BATTLE\n"
                                              "IF YOU DIE TO AN ENEMY IT'S GAMEOVER AND YOU WILL LOSE POINTS\n\n"
                                              "ATTACK:\nTHE DAMAGE YOU DO IS DEPENDENT ON YOUR ATTACK STAT, "
                                              "CRIT CHANCE, CRIT MULTIPLIER, AND YOUR OPPONENTS DEFENCE\n\n"
                                              "HEAL:\nHEALING IS DEPENDENT OF THE AFFECT STAT\n\n"
                                              "STAT BUFF AND NERF:\nBUFFING YOUR STATS AND NERFING YOUR OPPONENT'S"
                                              " STATS ARE BASED ON YOUR AFFECT STAT\n"
                                              "THE ONLY BUFF THAT IS NOT AFFECTED BY THE AFFECT STAT IS BUFFING"
                                              " THE AFFECT STAT\n\nPRESS ENTER IN THE CONSOLE TO CONTINUE\n")
                                    #else:

                YOUR_TURN = True

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
                player.move_up()
            if event.key == pygame.K_a:  # A
                player.move_left()
            if event.key == pygame.K_s:  # S
                player.move_down()
            if event.key == pygame.K_d:  # D
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