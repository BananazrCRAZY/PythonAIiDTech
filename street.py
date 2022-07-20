import pygame
import random
from bus import Bus
from ufo import UFO

class Street:
    SIZE = (600, 40)
    SCREEN_DIM = 600, 500

    def __init__(self, street_height: int, direction: str, number_of_buses: int):
        self.rect = pygame.Rect((0, street_height), Street.SIZE)
        self.buses = []

        self.add_buses(direction, number_of_buses, street_height+20)

    def add_buses(self, direction: str, number_of_buses: int, street_height: int):
        dp = []
        for _ in range(number_of_buses):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.buses.append(Bus((x_pos, street_height), direction))