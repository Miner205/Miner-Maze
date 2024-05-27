import pygame
from functions import convertbinaire
from random import randint


class Key:
    # key_number is like : "-:Red,-:Green,-:Blue", and 0 = 0 and 1 = 255.

    def __init__(self):
        self.number = convertbinaire(randint(0, 7), 3)
        self.image = pygame.image.load("images/keys/key_"+self.number+".png")
        #self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()


