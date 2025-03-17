import pygame
import functions
from maze import Maze
from player import Player
# from parameters import Options

# To run to start the game.

if __name__ == '__main__':
    print('PyCharm')


# # TO DO :
# Menu pour choisir la difficulté = change l'intervalle de la taille du labyrinthe/et du nombre de keys

# Time system (petite horloge de réveil pour le temps mis par le joueur)
# Score system
# Success system ?
# github
# Teleportation ?
# Minimap and Map ?
# Solo, mutli ?
# skins ?
# 42

# !!!!!!!!!!! To Cf for Maze Algorithms : https://www.youtube.com/watch?v=uctN47p_KVk !!!!!!!!!!


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
pygame.display.set_caption("Miner's Maze")
width, height = 1820, 980   # 1080, 720
screen = pygame.display.set_mode((width, height))   # , pygame.RESIZABLE

# background
# background = pygame.image.load("assets/background.jpeg")


running = True

player = Player(width//2, height//2)
maze = Maze("hard", player)
functions.print_matrix_nb(maze.rooms)

# For Maze debbug :
# maze.global_vision = True
# maze.minimap_global_vision = True

while running:

    # display the background
    pygame.draw.rect(screen, (0, 20, 60), (0, 0, width, height))
    # screen.blit(background, (0, 0))

    # get the current time
    current_time = pygame.time.get_ticks() // 1000
    # print the current time :
    font = pygame.font.SysFont("ArialBlack", 20)
    text = font.render('Time : {} s'.format(current_time), True, (0, 0, 0))
    screen.blit(text, (30, 20))

    if running:
        maze.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            maze.keys_pressed.add(event.key)

        if event.type == pygame.KEYUP:
            maze.keys_pressed.remove(event.key)

        maze.update(event)

    if running:
        maze.print(screen)

        # Update the screen
        pygame.display.flip()
        clock.tick(FPS)
