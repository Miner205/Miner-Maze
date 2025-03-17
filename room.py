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

        self.image = pygame.image.load("./images/rooms/room_" + self.number + ".png")
        # self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()

        # position in the maze ;; when the player move is the maze that move ??
        self.rect.center = (x, y)

        self.position = (0, 0)  # 0,0 = center of the maze ; -1,-1 : West-Nord ; 1,1 : Est-Sud.

        self.walls = get_walls(self.number, self.rect)

        # States :
        self.special = special   # None or "start" or "end"
        self.reversed = False  # faire des rooms 'inversé' : avec couleur et controles inversé ?
        self.visible = False   # /player nearby
        self.explored = False
        self.initialized = initialized   # For generation of the maze

    def update_visibility(self, player, vision_range):
        self.visible = abs(self.position[0]-player.position[0])+abs(self.position[1]-player.position[1]) <= vision_range
        if not self.explored and abs(self.position[0]-player.position[0])+abs(self.position[1]-player.position[1]) == 0:
            self.explored = True

    def print(self, screen):
        if self.visible:
            screen.blit(self.image, self.rect)

            if self.special == "start":
                pygame.draw.rect(screen, (0, 0, 255), (self.rect.x+32, self.rect.y+32, 22, 22))
            if self.special == "end":
                pygame.draw.rect(screen, (255, 0, 0), (self.rect.x+32, self.rect.y+32, 22, 22))
            if self.special == "teleport":
                pygame.draw.rect(screen, (150, 0, 255), (self.rect.x+32, self.rect.y+32, 22, 22))

        # for wall in self.walls:   # print walls ; use to change their colors or for debugging.
        #    pygame.draw.rect(screen, (255, 20, 50), wall)


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
