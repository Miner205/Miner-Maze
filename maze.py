import pygame
from random import randint
import functions
from room import Room
import key


# like game.py
class Maze:
    def __init__(self, difficulty, player):
        self.player = player
        self.keys_pressed = {}

        self.difficulty = difficulty   # easy, medium or hard
        if self.difficulty == "easy":
            self.size = 2*randint(1, 2)+1
        elif self.difficulty == "hard":
            self.size = 2*randint(3, 4)+1
        else:
            self.size = 2*randint(2, 3)+1
        self.rooms = generate_rooms(self.size, self.player)
        self.all_walls = []
        for row in range(self.size):
            for col in range(self.size):
                self.all_walls.append(self.rooms[row][col].walls)

    def run(self):
        #if self.rooms[row][col].visible:
        if self.keys_pressed.get(pygame.K_a):
            self.player.move_left(self.all_walls)
        if self.keys_pressed.get(pygame.K_d):
            self.player.move_right(self.all_walls)
        if self.keys_pressed.get(pygame.K_s):
            self.player.move_down(self.all_walls)
        if self.keys_pressed.get(pygame.K_w):
            self.player.move_up(self.all_walls)

    def update(self, event):
        #if self.rooms[row][col].visible:
        #self.player.update(event, self.all_walls)

        for row in range(self.size):
            for col in range(self.size):
                self.rooms[row][col].update(event, self.player)

    def print(self, screen):
        for row in range(self.size):
            for col in range(self.size):
                self.rooms[row][col].print(screen)
        self.player.print(screen)


def generate_rooms(size, player):
    rooms = [[Room(player.rect.x, player.rect.y) for _ in range(size)] for _ in range(size)]
    rooms[size // 2][size // 2] = Room(player.rect.x, player.rect.y, True, "1111", "start")
    for row in range(size):
        for col in range(size):
            criteria = rooms[row][col].number

            if row == 0:   # borders of maze are walls :
                criteria = new_number(criteria, "0000", 'sud')
            if row == size-1:
                criteria = new_number(criteria, "0000", 'nord')
            if col == 0:
                criteria = new_number(criteria, "0000", 'east')
            if col == size-1:
                criteria = new_number(criteria, "0000", 'west')

            # if neighbors are initialized, check there criteria to generate the criteria :
            if row != 0 and rooms[row-1][col].initialized:
                criteria = new_number(criteria, rooms[row-1][col].number, 'sud')
            if row != size-1 and rooms[row+1][col].initialized:
                criteria = new_number(criteria, rooms[row+1][col].number, 'nord')
            if col != 0 and rooms[row][col-1].initialized:
                criteria = new_number(criteria, rooms[row][col-1].number, 'east')
            if col != size-1 and rooms[row][col+1].initialized:
                criteria = new_number(criteria, rooms[row][col+1].number, 'west')

            rooms[row][col].modify(((-size//2)+col)*rooms[row][col].rect.w, ((-size//2)+row)*rooms[row][col].rect.h, True, criteria)

    return rooms


def new_number(new, number, direction_to_generate):
    if direction_to_generate == 'sud':
        tmp = list(new)
        tmp[3] = number[1]
        new = "".join(tmp)
    elif direction_to_generate == 'nord':
        tmp = list(new)
        tmp[1] = number[3]
        new = "".join(tmp)
    elif direction_to_generate == 'east':
        tmp = list(new)
        tmp[0] = number[2]
        new = "".join(tmp)
    elif direction_to_generate == 'west':
        tmp = list(new)
        tmp[2] = number[0]
        new = "".join(tmp)
    return new
