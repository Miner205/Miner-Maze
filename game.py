import pygame
from maze import Maze
from player import Player
import functions


class Game:
    def __init__(self, screen_width, screen_height, nb_of_floors):
        self.player = Player(screen_width // 2, screen_height // 2)
        self.current_maze = Maze("hard", self.player)
        self.floor = 0
        self.nb_of_floors = nb_of_floors
        functions.print_matrix_nb(self.current_maze.rooms)

        self.keys_pressed = set()

    def run(self):
        if pygame.K_LSHIFT in self.keys_pressed:  # run_key
            self.player.speed = 2  # note : rect stores only integers (rect of the position of the player)
        elif self.player.speed != 1:
            self.player.speed = 1
        if pygame.K_a in self.keys_pressed:
            self.player.move_left(self.current_maze.all_walls)
        if pygame.K_d in self.keys_pressed:
            self.player.move_right(self.current_maze.all_walls)
        if pygame.K_s in self.keys_pressed:
            self.player.move_down(self.current_maze.all_walls)
        if pygame.K_w in self.keys_pressed:
            self.player.move_up(self.current_maze.all_walls)

        if self.keys_pressed:
            old_pos = self.player.position
            self.player.update_position(self.current_maze.rooms, self.current_maze.size)
            # print("position : " + str(self.player.position))  # use for debugging.

            if self.player.position != old_pos:
                self.current_maze.update_rooms_visibility(self.player)

    def update(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.current_maze.update(event)

            if self.current_maze.maze_ended:
                ...

    def print(self, screen):
        self.current_maze.print(screen)
        self.player.print(screen)
        self.current_maze.minimap.print(screen, self.player.position)
