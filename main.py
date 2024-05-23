import pygame
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
# Minimap
# Solo, mutli ?
# skins ?


pygame.init()

# Define a clock
clock = pygame.time.Clock()
FPS = 60

# Create a window
pygame.display.set_caption("Miner's Maze")
width, height = 1080, 720
screen = pygame.display.set_mode((width, height))   # , pygame.RESIZABLE

# background
# background = pygame.image.load("assets/background.jpeg")

running = True

maze = Maze()
player = Player()


while running:

    # get the current time
    current_time = pygame.time.get_ticks() // 1000

    # display the background
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1080, 720))
    # screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()

        maze.update()

    maze.print()

    # Update the screen
    if running:
        pygame.display.flip()
        clock.tick(FPS)
