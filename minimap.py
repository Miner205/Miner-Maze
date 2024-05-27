import pygame


class Minimap:

    def __init__(self):
        self.explored_room = []


    def print(self, screen, player_pos):
        pygame.draw.rect(screen, (70, 45, 50), (screen.get_width() - 160, 32, 128, 128))

        rect = pygame.Rect(screen.get_width() - 160, 32, 128, 128).center
        new_rect = pygame.Rect((rect[0]-4, rect[1]-4, 8, 8))
        for room in self.explored_room:
            if room.special == "start":
                color = (0, 0, 255)
            elif room.special == "end":
                color = (255, 0, 0)
            elif room.special == "teleport":
                color = (150, 0, 255)
            else:
                color = (255, 255, 255)
            pygame.draw.rect(screen, color, (new_rect.x+room.position[0]*(new_rect.w+2),
                                             new_rect.y+room.position[1]*(new_rect.h+2), new_rect.w, new_rect.h))
            pygame.draw.rect(screen, (255, 50, 0), (new_rect.x+player_pos[0]*(new_rect.w+2)+new_rect.w//4,
                                                    new_rect.y+player_pos[1]*(new_rect.h+2)+new_rect.h//4, new_rect.w//2, new_rect.h//2))

