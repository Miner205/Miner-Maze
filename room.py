import pygame
from functions import convertbinaire
from random import randint


class Room:
    # room_number is like : "-:West,-:Sud,-:Est,-:Nord", and if - = 0 there is a wall, if - = 1 there is a door.

    def __init__(self, x=0, y=0, initialized=False, criteria=None, special=None):
        # all rooms : self.rooms = [pygame.image.load("images/rooms/room_"+convertbinaire(i, 4)+".png") for i in range(16)]

        self.number = convertbinaire(randint(0, 15), 4)
        if criteria is not None:  # exemple criteria : "-1--"
            for i in range(4):
                if criteria[i] == '1' or criteria[i] == '0':
                    tmp = list(self.number)
                    tmp[i] = criteria[i]
                    self.number = "".join(tmp)
                else:
                    tmp = list(self.number)
                    tmp[i] = randint(0, 1)
                    self.number = "".join(tmp)

        self.image = pygame.image.load("images/rooms/room_" + self.number + ".png")
        # self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()
        #self.rect.center = (x, y)   # position in the maze ;; when the player move is the maze that move ??
        self.rect.topleft = (x+self.rect.w//2+5, y+self.rect.h//2+5)

        self.walls = get_walls(self.number, self.rect)

        # States :
        self.special = special   # None or "start" or "end"
        self.reversed = False  # faire des rooms 'inversé' : avec couleur et controles inversé ?
        self.visible = False   # /player nearby
        self.explored = False
        self.initialized = initialized   # For generation of the maze

    def update(self, event, player):
        self.visible = self.player_nearby(player)

    def print(self, screen):
        #if self.visible:
        screen.blit(self.image, self.rect)

        # for wall in self.walls:   # print walls ; use to change their colors or debugging.
        #    pygame.draw.rect(screen, (255, 20, 50), wall)

    def player_nearby(self, player):
        if abs(self.rect.x-player.rect.x) <= 2*self.rect.w and abs(self.rect.y-player.rect.y) <= 2*self.rect.h:
            return True
        else:
            return False

    def modify(self, x=0, y=0, initialized=False, criteria=None, special=None):
        if x != 0:
            self.rect.x += x
        if y != 0:
            self.rect.y += y
        if criteria is not None:  # exemple criteria : "-1--"
            for i in range(4):
                if criteria[i] == '1' or criteria[i] == '0':
                    tmp = list(self.number)
                    tmp[i] = criteria[i]
                    self.number = "".join(tmp)
                else:
                    tmp = list(self.number)
                    tmp[i] = randint(0, 1)
                    self.number = "".join(tmp)

            self.walls = get_walls(self.number, self.rect)
        self.image = pygame.image.load("images/rooms/room_" + self.number + ".png")
        # self.image = pygame.transform.scale()
        if special is not None:
            self.special = special
        self.initialized = initialized


def get_walls(number, room_rect):
    walls = []

    if number[0] == '1':   # West
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 5, 32))
        walls.append(pygame.Rect(room_rect.x, room_rect.y+54, 5, 32))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 5, 86))

    if number[1] == '1':   # Sud
        walls.append(pygame.Rect(room_rect.x, room_rect.y+room_rect.h-5, 32, 5))
        walls.append(pygame.Rect(room_rect.x+54, room_rect.y+room_rect.h-5, 32, 5))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y+room_rect.h-5, 86, 5))

    if number[2] == '1':   # Est
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y, 5, 32))
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y+54, 5, 32))
    else:
        walls.append(pygame.Rect(room_rect.x+room_rect.w-5, room_rect.y, 5, 86))

    if number[3] == '1':   # Nord
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 32, 5))
        walls.append(pygame.Rect(room_rect.x+54, room_rect.y, 32, 5))
    else:
        walls.append(pygame.Rect(room_rect.x, room_rect.y, 86, 5))

    return walls
