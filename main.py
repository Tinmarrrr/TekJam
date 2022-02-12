##
# EPITECH PROJECT, 2022
# TekJam
# File description:
# menu
##

import pygame
import pygame_menu
from src import Character

WIDTH = 1280
HEIGHT = 720

def start_the_game():

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gorille.nextText()
                if event.key == pygame.K_RIGHT:
                    clodo.nextText()

        surface.fill((255, 255, 255))
        surface.blit(gorille.sprite, gorille.rect)
        surface.blit(clodo.sprite, clodo.rect)
        surface.blit(gorille.currentText, (200, 200))
        surface.blit(clodo.currentText, (800, 200))

        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    tab1 = ["OUG", "OUG OUG", "OUG OUG OUG"]
    tab2 = ["T'AS", "PAS UNE", "CLOPE STP???"]
    gorille = Character.Character("assets/gorilla/gorilla_base.png", [100, 300], tab1, font)
    clodo = Character.Character("assets/enemies/full_clodo.png", [900, 300], tab2, font)


    pygame.mixer.music.load("assets/Music/main_theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.6)

    menu = pygame_menu.Menu('LA JOUTE', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', start_the_game)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
