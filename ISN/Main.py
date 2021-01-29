import pygame
import os
from pygame.locals import *
import pygame

pygame.init()   #intialisation pygame

#boucle générale :____________________________________________________________________________
try:
    #variables____________________________________________________________________________________
    w = pygame.display.Info().current_w
    h = pygame.display.Info().current_h
    a = 32
    xd = 0
    yd = 0
    # constantes de couleurs
    blanc = (255, 255, 255)
    marron = (153, 76, 0)
    vert = (0, 255, 0)
    # constantes representant les différentes fonction
    T1 = 0
    T2 = 1
    T3 = 2

    # dictionnaire qui defini les différentes textures
    textures = {
        T1: pygame.image.load('sol.png'),
        T2: pygame.image.load('noir.png'),
        T3: pygame.image.load('mur.png'),
    }

# la map
    tilemap = [
        [T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2],
        [T2, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T3, T3, T1, T1, T1, T3, T3, T1, T3, T3, T1, T1, T1, T1, T1, T3, T3, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T3, T3, T3, T1, T3, T3, T1, T3, T3, T1, T3, T3, T3, T3, T1, T1, T1, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T3, T3, T3, T1, T3, T3, T3, T1, T3, T3, T1, T3, T3, T3, T1, T1, T1, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T3, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T3, T3, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T3, T3, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T3, T3, T1, T3, T3, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T3, T3, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T3, T3, T3, T3, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T1, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T3, T3, T3, T1, T1, T3, T3, T3, T1, T3, T3, T3, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T3, T1, T1, T3, T1, T1, T1, T3, T3, T1, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T1, T3, T3, T3, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T3, T3, T3, T1, T3, T3, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T1, T3, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T3, T3, T3, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T2],
        [T2, T1, T1, T3, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T1, T1, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T3, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T1, T2],
        [T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2, T2],
                    
        ]

    # taille de la map
    TAILLECASES = 64
    MAPLARGE = 68
    MAPHAUTEUR = 45

#fenetre______________________________________________________________________________________
    os.environ['SDL_VIDEO_WINDOW_POS']="0,0" #positionnement de la fenetre
    fenetre=pygame.display.set_mode((0,0),pygame.FULLSCREEN) #taille de la fenetre

#chargement personnage________________________________________________________________________
    image1=pygame.image.load("perso_face_2.png")
    image1=pygame.transform.scale(image1,(29,63)) #19x42
    image1_rect=image1.get_rect()
    fenetre.blit(image1, (w/2,h/2))
    pygame.key.set_repeat(1,10)
    continuer=1

#lecture de la musique________________________________________________________________________
    pygame.mixer.music.load('musique.mp3')
    pygame.mixer.music.play(loops = -1)

    map_surface = pygame.Surface((len(tilemap[0]) * TAILLECASES, len(tilemap) * TAILLECASES))

#boucle fenetre_______________________________________________________________________________
    while continuer:
#fermer la fenetre____________________________________________________________________________
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer=0
#-----------------ou-------------------------------------------------------------------------#
            elif event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    continuer=0
                    
#déplacement vers la gauche__________________________________________________________________
                elif event.key==K_a:
                    
                    xd = xd + 5
                    a = a-1
                    if a == 24:
                        image1=pygame.image.load("perso_gauche_1.png") 
                        image1=pygame.transform.scale(image1,(68,57)) #45x38
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 16:
                        image1=pygame.image.load("perso_gauche_2.png") 
                        image1=pygame.transform.scale(image1,(68,62)) #45x41
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 8:
                        image1=pygame.image.load("perso_gauche_3.png") 
                        image1=pygame.transform.scale(image1,(68,63)) #45x42
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 0:
                        image1=pygame.image.load("perso_gauche_2.png") 
                        image1=pygame.transform.scale(image1,(68,62)) #45x41
                        fenetre.blit(image1, (w/2,h/2))
                        a = 32

#déplacement vers la droite___________________________________________________________________
                elif event.key==K_d:
                    
                    xd = xd -5
                    a = a-1
                    if a == 24:
                        image1=pygame.image.load("perso_droite_1.png") 
                        image1=pygame.transform.scale(image1,(68,63)) #45x42
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 16:
                        image1=pygame.image.load("perso_droite_2.png") 
                        image1=pygame.transform.scale(image1,(68,62)) #45x41
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 8:
                        image1=pygame.image.load("perso_droite_3.png") 
                        image1=pygame.transform.scale(image1,(68,57)) #45x38
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 0:
                        image1=pygame.image.load("perso_droite_2.png")
                        image1=pygame.transform.scale(image1,(68,62)) #45x41
                        fenetre.blit(image1, (w/2,h/2))
                        a = 32

#déplacement vers le bas______________________________________________________________________
                if event.key==K_s:

                    yd = yd -5
                    a = a-1
                    if a == 24:
                        image1=pygame.image.load("perso_face_1.png") 
                        image1=pygame.transform.scale(image1,(29,62)) #19x41
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 16:
                        image1=pygame.image.load("perso_face_2.png") 
                        image1=pygame.transform.scale(image1,(29,63)) #19x42
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 8:
                        image1=pygame.image.load("perso_face_3.png") 
                        image1=pygame.transform.scale(image1,(29,62)) #19x41
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 0:
                        image1=pygame.image.load("perso_face_2.png") 
                        image1=pygame.transform.scale(image1,(29,63)) #19x42
                        fenetre.blit(image1, (w/2,h/2))
                        a = 32
                        
#déplacement vers le haut_____________________________________________________________________
                if event.key==K_w:

                    yd = yd +5
                    a = a-1
                    if a == 24:
                        image1=pygame.image.load("perso_dos_1.png") 
                        image1=pygame.transform.scale(image1,(30,63)) #20x42
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 16:
                        image1=pygame.image.load("perso_dos_2.png") 
                        image1=pygame.transform.scale(image1,(26,62)) #17x41
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 8:
                        image1=pygame.image.load("perso_dos_3.png") 
                        image1=pygame.transform.scale(image1,(30,63)) #20x42
                        fenetre.blit(image1, (w/2,h/2))
                    elif a == 0:
                        image1=pygame.image.load("perso_dos_2.png") 
                        image1=pygame.transform.scale(image1,(26,62)) #17x41
                        fenetre.blit(image1, (w/2,h/2))
                        a = 32

#rafraichissement de l'affichage______________________________________________________________
        pygame.display.flip()   #refresh général
        for ligne in range(MAPHAUTEUR):
            for colone in range(MAPLARGE): #loop through each column in the row
               fond=fenetre.blit(textures[tilemap[ligne][colone]],(colone * TAILLECASES + xd   , ligne * TAILLECASES + yd  , TAILLECASES, TAILLECASES)) #construit la map avec les bonnes textures
        fenetre.blit(image1, (w/2,h/2)) #refresh perso    
        pygame.display.update() #rafraichisement de la fenetre
        
#Collisions___________________________________________________________________________________

#fin__________________________________________________________________________________________
except:
    traceback.print_exc()
finally:
    pygame.quit()
    exit()
