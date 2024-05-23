import pygame
from random import randint


class Key:
    # key_number is like : "-:Red,-:Green,-:Blue", and 0 = 0 and 1 = 255.

    def __init__(self):
        self.number = convertbinaire(randint(0, 7), 3)
        self.image = pygame.image.load("images/keys/key_"+self.number+".png")
        #self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()


def convertbinaire(x, k):
    """convert integers(int), between 0 and 2^k-1, into binary(string), on k digits."""
    result = ""
    while x != 0:
        result = str(x % 2) + result
        x //= 2
    result = '0'*(k-len(result)) + result
    return result
