import pygame
from functions import convertbinaire
from random import randint
from math import sin


class Item:
    # key, torch, etc.
    def __init__(self, name, x, y):
        self.name = name
        self.image = pygame.image.load("./images/items/" + self.name + ".png")
        # self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()
        self.y_0 = y
        self.rect.x, self.rect.y = x, y


    def print(self, screen):
        amplitude = 5   # Amplitude of vertical oscillation
        frequency = 0.5   # Oscillation frequency
        current_time = pygame.time.get_ticks() // 1000   # get the current time
        # Calculate vertical position based on the time
        self.rect.y = self.y_0 + amplitude * sin(frequency * current_time)

        if self.visible:
            screen.blit(self.image, self.rect)


class Key(Item):  # extension of Item
    # key_number is like : "-:Red,-:Green,-:Blue", and 0 = 0 and 1 = 255.

    def __init__(self, x, y):
        super().__init__("key_"+convertbinaire(randint(0, 7), 3), x, y)

