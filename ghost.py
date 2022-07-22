import pygame, random


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

    affect = 1.0
    crit_chance = 20.0
    crit_mult = 1.5

    def __init__(self, position: tuple, MOVE_DIST: int, stealth: int, hp, attack, defence, speed):
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
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.speed = speed

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

    def calc_dmg(self, ene_def):
        if random.randint(0, 100) < self.crit_chance:
            dmg = (self.attack * self.crit_mult) - (ene_def / 10)
        else:
            dmg = self.attack - (ene_def / 10)
        return dmg

    def heal(self):
        self.hp += 10 * self.affect
        if self.hp > 100:
            self.hp = 100.0
        print("ENEMY HEALED\nENEMY HP: " + str(self.hp) + "\n")

    def get_stats(self):
        print("ENEMY:")
        print("HP: " + str(self.hp))
        print("DMG: " + str(self.attack))
        print("DEF: " + str(self.defence))
        print("SPD: " + str(self.speed))
        print("AFF: " + str(self.affect))
        print("CRIT_CHC: " + str(self.crit_chance))
        print("CRIT_MULT: " + str(self.crit_mult))
        print()

    def buff_attack(self):
        self.attack += 2 * self.affect
        if self.attack > 40:
            self.attack = 40
        print("ENEMY INCREASED ATTACK: " + str(self.attack) + "\n")

    def buff_defence(self):
        self.defence += 2 * self.affect
        if self.defence > 20:
            self.defence = 20
        print("ENEMY INCREASED DEFENCE: " + str(self.defence) + "\n")

    def buff_speed(self):
        self.speed += 2 * self.affect
        if self.speed > 20:
            self.speed = 20
        print("ENEMY INCREASED SPEED: " + str(self.speed) + "\n")

    def buff_affect(self):
        self.affect += 0.1
        if self.affect > 2:
            self.affect = 2
        print("ENEMY INCREASED AFFECT: " + str(self.affect) + "\n")

    def buff_crit_chance(self):
        self.crit_chance += 10 * self.affect
        if self.crit_chance > 90:
            self.crit_chance = 90
        print("ENEMY INCREASED CRITICAL CHANCE: " + str(self.crit_chance) + "%\n")

    def buff_crit_mult(self):
        self.crit_mult += 0.1
        if self.crit_mult > 2:
            self.crit_mult = 2
        print("ENEMY INCREASED CRITICAL MULTIPLIER: x" + str(self.crit_mult) + "\n")

    def nerf_attack(self, ene_affect):
        self.attack -= 2 * ene_affect
        if self.attack < 10:
            self.attack = 10
        print("ENEMY ATTACK DECREASED: " + str(self.attack) + "\n")

    def nerf_defence(self, ene_affect):
        self.defence -= 2 * ene_affect
        if self.defence < 1:
            self.defence = 1
        print("ENEMY DEFENCE DECREASED: " + str(self.defence) + "\n")

    def nerf_speed(self, ene_affect):
        self.speed -= 2 * ene_affect
        if self.speed < 1:
            self.speed = 1
        print("ENEMY SPEED DECREASED: " + str(self.speed) + "\n")

    def nerf_affect(self):
        self.affect -= 0.1
        if self.affect < 0:
            self.affect = 0
        print("ENEMY AFFECT DECREASED: " + str(self.affect) + "\n")

    def nerf_crit_chance(self, ene_affect):
        self.crit_chance -= 10 * ene_affect
        if self.crit_chance < 0:
            self.crit_chance = 0
        print("ENEMY CRITICAL CHANCE DECREASED: " + str(self.crit_chance) + "%\n")

    def nerf_crit_mult(self):
        self.crit_mult -= 0.1
        if self.crit_mult < 1:
            self.crit_mult = 1
        print("ENEMY CRITICAL MULTIPLIER DECREASED: x" + str(self.crit_mult) + "\n")
