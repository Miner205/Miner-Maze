import pygame


class Player:
    # Player.

    def __init__(self, x, y):
        self.image = pygame.image.load("images/player.png")
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 1
        self.position = (0, 0)   # 0,0 = center of the maze ; -1,-1 : West-Nord ; 1,1 : Est-Sud.

    """def update(self, event, all_walls):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.move_left(all_walls)
            if event.key == pygame.K_d:
                self.move_right(all_walls)
            if event.key == pygame.K_s:
                self.move_down(all_walls)
            if event.key == pygame.K_w:
                self.move_up(all_walls)"""

    def print(self, screen):
        screen.blit(self.image, self.rect)

    def move_right(self, all_walls):
        if not self.wall_collision(all_walls, 'right'):
            self.rect.x += self.speed

    def move_left(self, all_walls):
        if not self.wall_collision(all_walls, 'left'):
            self.rect.x -= self.speed

    def move_up(self, all_walls):
        if not self.wall_collision(all_walls, 'up'):
            self.rect.y -= self.speed

    def move_down(self, all_walls):
        if not self.wall_collision(all_walls, 'down'):
            self.rect.y += self.speed

    def wall_collision(self, all_walls, direction):
        for room_walls in all_walls:
            for wall in room_walls:
                if direction == 'right':
                    if wall.colliderect(self.rect.x+self.speed, self.rect.y, self.rect.w, self.rect.h):
                        return True
                if direction == 'left':
                    if wall.colliderect(self.rect.x-self.speed, self.rect.y, self.rect.w, self.rect.h):
                        return True
                if direction == 'up':
                    if wall.colliderect(self.rect.x, self.rect.y-self.speed, self.rect.w, self.rect.h):
                        return True
                if direction == 'down':
                    if wall.colliderect(self.rect.x, self.rect.y+self.speed, self.rect.w, self.rect.h):
                        return True

        return False

    def update_position(self, all_rooms, size):
        for row in range(size):
            for col in range(size):
                if all_rooms[row][col].rect.colliderect(self.rect):
                    self.position = (((-size//2)+col+1), ((-size//2)+row+1))
