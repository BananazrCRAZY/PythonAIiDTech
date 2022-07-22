import pygame, random

class Player(pygame.sprite.Sprite):
    STARTING_POSITION = (300, 300)
    SIZE = (20, 20)
    IMAGE = pygame.image.load('resources/player.png')
    MOVE_DIST = 20
    SCREEN_DIM = 600, 600
    DEAD = False

    hp = 100.0
    attack = 20.0
    defence = 10.0
    speed = 10.0
    affect = 1.0
    # convert this to %
    crit_chance = 20.0
    crit_mult = 1.5

    def __init__(self, name):
        super().__init__()
        self.image = Player.IMAGE
        self.name = name
        self.rect = pygame.Rect((0, 0), Player.SIZE)
        self.rect.center = Player.STARTING_POSITION

    def move_up(self):
        if self.rect.top >= 20:
            self.rect.centery -= Player.MOVE_DIST

    def move_down(self):
        if self.rect.bottom <= 580:
            self.rect.centery += Player.MOVE_DIST

    def move_left(self):
        if self.rect.left >= 20:
            self.rect.centerx -= Player.MOVE_DIST

    def move_right(self):
        if self.rect.right <= 580:
            self.rect.centerx += Player.MOVE_DIST

    def calc_dmg(self, ene_def):
        if random.randint(0, 100) < self.crit_chance:
            dmg = (self.attack * self.crit_mult) - (ene_def/10)
        else:
            dmg = self.attack - (ene_def / 10)
        return dmg

    def heal(self):
        self.hp += 10 * self.affect
        if self.hp > 100:
            self.hp = 100.0
        print("YOU HEALED\nYOUR HP: " + str(self.hp) + "\n")

    def get_stats(self):
        print(self.name + ":")
        print("HP: " + str(self.hp))
        print("DMG: " + str(self.attack))
        print("DEF: " + str(self.defence))
        print("SPD: " + str(self.speed))
        print("AFF: " + str(self.affect))
        print("CRIT_CHC: " + str(self.crit_chance))
        print("CRIT_MULT: " + str(self.crit_mult))
        print()

    def reset_stats(self):
        self.attack = 10.0
        self.defence = 10.0
        self.speed = 10.0
        self.affect = 1.0
        self.crit_chance = 10.0
        self.crit_mult = 1.5

    def buff_attack(self):
        self.attack += 2 * self.affect
        if self.attack > 40:
            self.attack = 40
        print("INCREASED YOUR ATTACK: " + str(self.attack) + "\n")

    def buff_defence(self):
        self.defence += 2 * self.affect
        if self.defence > 20:
            self.defence = 20
        print("INCREASED YOUR DEFENCE: " + str(self.defence) + "\n")

    def buff_speed(self):
        self.speed += 2 * self.affect
        if self.speed > 20:
            self.speed = 20
        print("INCREASED YOUR SPEED: " + str(self.speed) + "\n")

    def buff_affect(self):
        self.affect += 0.1
        if self.affect > 2:
            self.affect = 2
        print("INCREASED YOUR AFFECT: " + str(self.affect) + "\n")

    def buff_crit_chance(self):
        self.crit_chance += 10 * self.affect
        if self.crit_chance > 90:
            self.crit_chance = 90
        print("INCREASED YOUR CRITICAL CHANCE: " + str(self.crit_chance) + "%\n")

    def buff_crit_mult(self):
        self.crit_mult += 0.1
        if self.crit_mult > 2:
            self.crit_mult = 2
        print("INCREASED YOUR CRITICAL MULTIPLIER: x" + str(self.crit_mult) + "\n")

    def nerf_attack(self, ene_affect):
        self.attack -= 2 * ene_affect
        if self.attack < 10:
            self.attack = 10
        print("ENEMY DECREASED YOUR ATTACK: " + str(self.attack) + "\n")

    def nerf_defence(self, ene_affect):
        self.defence -= 2 * ene_affect
        if self.defence < 1:
            self.defence = 1
        print("ENEMY DECREASED YOUR DEFENCE: " + str(self.defence) + "\n")

    def nerf_speed(self, ene_affect):
        self.speed -= 2 * ene_affect
        if self.speed < 1:
            self.speed = 1
        print("ENEMY DECREASED YOUR SPEED: " + str(self.speed) + "\n")

    def nerf_affect(self):
        self.affect -= 0.1
        if self.affect < 0:
            self.affect = 0
        print("ENEMY DECREASED YOUR AFFECT: " + str(self.affect) + "\n")

    def nerf_crit_chance(self, ene_affect):
        self.crit_chance -= 10 * ene_affect
        if self.crit_chance < 0:
            self.crit_chance = 0
        print("ENEMY DECREASED YOUR CRITICAL CHANCE: " + str(self.crit_chance) + "%\n")

    def nerf_crit_mult(self):
        self.crit_mult -= 0.1
        if self.crit_mult < 1:
            self.crit_mult = 1
        print("ENEMY DECREASED YOUR CRITICAL MULTIPLIER: x" + str(self.crit_mult) + "\n")
