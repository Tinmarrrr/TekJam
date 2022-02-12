##
# EPITECH PROJECT, 2022
# TekJam
# File description:
# menu
##

import pygame
import pygame_menu
from src import character

WIDTH = 1280
HEIGHT = 720

def start_the_game():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        surface.fill((255, 255, 255))
        surface.blit(gorille.sprite, gorille.rect)
        surface.blit(gros.sprite, gros.rect)

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    surface = pygame.display.set_mode((WIDTH, HEIGHT))
    gorille = character.Character("assets/gorille.png", [100, 300])
    gros = character.Character("assets/full_clodo.png", [900, 300])

    menu = pygame_menu.Menu('LA JOUTE', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
