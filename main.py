##
# EPITECH PROJECT, 2022
# TekJam
# File description:
# menu
##

import pygame
import sys
import pygame_menu

def start_the_game():
    pass

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    menu = pygame_menu.Menu('LA JOUTE', 600, 400,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
