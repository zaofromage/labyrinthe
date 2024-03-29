import pygame
import sys
import time
from laby import *

pygame.init()

lab = create_lab(lab_alea(20, 100))

fps = 60
fpsClock = pygame.time.Clock()

mur = 'X'
joueur = 'A'
ancien = (0, 0)
perso = (1, 0)
path = set()
perm = False
snake = []
 
tileSize = 50
width, height = len(lab)*tileSize, len(lab)*tileSize
screen = pygame.display.set_mode((width, height))

def deplacement(lab, perso, path):
    possible = True
    if (lab[perso[0], perso[1]+1] != 'X' and (perso[0], perso[1]+1) not in path):
        perso = (perso[0], perso[1]+1)
    elif (lab[perso[0]+1, perso[1]] != 'X' and (perso[0]+1, perso[1]) not in path):
        perso = (perso[0]+1, perso[1])
    elif (lab[perso[0]-1, perso[1]] != 'X' and (perso[0], perso[1]-1) not in path):
        perso = (perso[0]-1, perso[1])
    elif (lab[perso[0], perso[1]-1] != 'X' and (perso[0]-1, perso[1]) not in path):
        perso = (perso[0], perso[1]-1)
    else:
        possible = False
    return perso, possible



while True:
    screen.fill((255, 255, 255))

    for i in range(len(lab)):
        for j in range(len(lab)):
            if lab[i][j] == mur:
                pygame.draw.rect(screen, (0, 0, 0), [j*tileSize, i*tileSize, tileSize, tileSize])
            if lab[i][j] == joueur:
                pygame.draw.rect(screen, (0, 255, 0), [j*tileSize, i*tileSize, tileSize, tileSize])
    for pos in snake:
        pygame.draw.rect(screen, (24, 163, 198), [pos[1]*tileSize, pos[0]*tileSize, tileSize, tileSize])
    lab[perso] = ' '
    ancien = perso
    perso = deplacement(lab, perso, path)[0]
    path.update([perso])
    lab[perso] = joueur
    time.sleep(0.2)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
  
    
    fpsClock.tick(fps)