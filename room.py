import pygame
from key import convertbinaire
from random import randint


class Room:
    # room_number is like : "-:West,-:Sud,-:Est,-:Nord", and if - = 0 there is a wall, if - = 1 there is a door.

    def __init__(self, special=None, criteria=None):
        # all rooms : self.rooms = [pygame.image.load("images/rooms/room_"+convertbinaire(i, 4)+".png") for i in range(16)]
        self.number = convertbinaire(randint(0, 15), 4)
        if criteria is not None:  # exemple criteria : "-1--"
            for i in range(4):
                if criteria[i] == '1' or criteria[i] == '0':
                    self.number[i] = criteria[i]
                else:
                    self.number[i] = randint(0, 1)
        self.image = pygame.image.load("images/rooms/room_" + self.number + ".png")
        # self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()
        #self.rect.x =  position in the maze ;; when the player move is the maze that move ??
        #self.rect.y =  position in the maze
        self.special = special   # None or "start" or "end"
        self.reversed = False  # faire des rooms 'inversé' : avec couleur et controles inversé ?
        self.visible = False
        self.explored = False
        self.walls = get_walls(self.number, self.rect)

    def update(self, event, player):

    def print(self, screen):

def get_walls(number, room_rect):
    walls = []

    if number[0]:   # West
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 5, 32))
        walls.append(pygame.Rect(room_rect.x, room_rect.y+54, 5, 32))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 5, 86))

    if number[1]:   # Sud
        walls.append(pygame.Rect(room_rect.x, room_rect.y+room_rect.h-5, 32, 5))
        walls.append(pygame.Rect(room_rect.x+54, room_rect.y+room_rect.h-5, 32, 5))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y+room_rect.h-5, 86, 5))

    if number[2]:   # Est
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y, 5, 32))
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y+54, 5, 32))
    else:
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y, 5, 86))

    if number[3]:   # Nord
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 32, 5))
        walls.append(pygame.Rect(room_rect.x+54, room_rect.y, 32, 5))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 86, 5))

    return walls
