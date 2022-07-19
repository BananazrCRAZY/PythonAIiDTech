import random
class Bots:
    def __init__(self, name, enemy_def):
        self.enemy_def = enemy_def
        self.name = name
        self.health = 100
        self.base_damage = 10
        self.base_armor = 5
        self.speed = 10
        self.dead = False

    def attack(self, opponent):
        dmg = self.base_damage - (self.base_damage * self.enemy_def/100)
        opponent.take_damage(dmg)

    def take_damage(self, damage_dealt):
        if damage_dealt < 1:
            self.health -= 1
        else:
            self.health -= damage_dealt

        if self.health <= 0:
            self.dead = True

    def get_stats(self):
        print(self.name + ":")
        print("DMG: " + str(self.base_damage))
        print("ARMOR: " + str(self.base_armor))
        print("SPD: " + str(self.speed))
        print("HP: " + str(self.health))
        print()

    def build_damage(self):
        self.base_damage += 2
        if self.base_damage > 20:
            self.base_damage = 20

    def build_armor(self):
        self.base_armor += 1
        if self.base_armor > 10:
            self.base_armor = 10

    def build_speed(self):
        self.speed += 2
        if self.speed > 20:
            self.speed = 20

    def heal(self):
        self.health += 7
        self.speed -= 1
        if self.health >= 100:
            self.health = 100

    def decrease_damage(self, opponent):
        opponent.base_damage -= 2
        self.health -= 5
        if opponent.base_damage < 1:
            opponent.base_damage = 1

    def decrease_armor(self, opponent):
        opponent.base_armor -= 1
        self.health -= 5
        if opponent.base_armor < 1:
            opponent.base_armor = 1

    def decrease_speed(self, opponent):
        opponent.speed -= 2
        self.health -= 5
        if opponent.speed < 1:
            opponent.speed = 1

    def action(self, opponent):
        random_num = random.randint(0, 100)
        if random_num <= 5:
            self.build_armor()
            print(self.name + " increased defense")
        elif random_num <= 30:
            self.build_damage()
            print(self.name + " increased damage")
        elif random_num <= 35:
            self.build_speed()
            print(self.name + " increased speed")
        elif random_num <= 50:
            opponent.decrease_damage(opponent)
            print(self.name + " decreased your damage")
        elif random_num <= 55:
            opponent.decrease_speed(opponent)
            print(self.name + " decreased your speed")
        elif random_num <= 60:
            opponent.decrease_armor(opponent)
            print(self.name + " decreased your defense")
        elif random_num <= 75:
            self.heal()
            print(self.name + " healed")
        else:
            self.attack(opponent)
            print(self.name + " attacked")

    def is_alive(self):
        if self.health <= 0:
            return False
        else:
            return True