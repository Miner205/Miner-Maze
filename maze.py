import pygame
from room import Room
import key

# like game.py


class Maze:
    def __init__(self, size):
        self.rooms #= [[0 for i in range(size)] for j in range(size)]
        self.rooms[size//2][size//2] = Room("start", "1111")



    def update(self, event, player):
        player.update(event)

    def print(self, screen, player):
