import pygame


class Player:
    # Player.

    def __init__(self, x, y):
        self.image = pygame.image.load("images/player.png")
        #self.image = pygame.transform.scale()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1

    def update(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left()
            if event.key == pygame.K_d:
                self.move_right()
            if event.key == pygame.K_s:
                self.move_down()
            if event.key == pygame.K_w:
                self.move_up()

    def print(self, screen):

    def move_right(self, room_walls):
        for wall in room_walls:
            if not wall.collidepoint((self.rect.x+self.speed, self.rect.y)):
                self.rect.x += self.speed

    def move_left(self, room_walls):
        for wall in room_walls:
            if not wall.collidepoint((self.rect.x-self.speed, self.rect.y)):
                self.rect.x -= self.speed

    def move_up(self, room_walls):
        for wall in room_walls:
            if not wall.collidepoint((self.rect.x, self.rect.y-self.speed)):
                self.rect.y -= self.speed

    def move_down(self, room_walls):
        for wall in room_walls:
            if not wall.collidepoint((self.rect.x, self.rect.y+self.speed)):
                self.rect.y += self.speed
