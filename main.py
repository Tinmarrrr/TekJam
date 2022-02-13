##
# EPITECH PROJECT, 2022
# TekJam
# File description:
# menu
##

import pygame
import pygame_menu
from src.character import Character

WIDTH = 1280
HEIGHT = 720

def choose_menu():
    w, h = pygame.display.get_surface().get_size()
    ##gorille
    gorille = Character("assets/gorilla/gorilla_base.png",
                        "assets/gorilla/gorilla_base.png", [100, 300], tab1, font)
    ##clodo
    clodo = Character("assets/enemies/full_clodo.png",
                      "assets/enemies/head_clodo.png", [900, 300], tab2, font)
    clodo_button = pygame.Rect(10, 10, 300, 300)
    clodo_surf = pygame.Surface(clodo_button.size)
    ##titi
    titi = Character("assets/enemies/full_titi.png",
                     "assets/enemies/head_titi.png", [900, 300], tab2, font)
    titi_button = pygame.Rect(((w - 300) / 2), 10, 300, 300)
    titi_surf = pygame.Surface(titi_button.size)
    ##ronald
    ronald = Character("assets/enemies/full_ronald.png",
                       "assets/enemies/head_ronald.png", [900, 300], tab2, font)
    ronald_button = pygame.Rect(10, (h - 300), 300, 300)
    ronald_surf = pygame.Surface(ronald_button.size)
    ##maman
    maman = Character("assets/enemies/full_maman_enfant.png",
                      "assets/enemies/head_maman_enfant.png", [900, 300], tab2, font)
    maman_button = pygame.Rect(((w - 300) / 2), (h - 300), 300, 300)
    maman_surf = pygame.Surface(maman_button.size)
    #gaston
    gaston = Character("assets/enemies/full_gaston.png",
                       "assets/enemies/head_gaston.png", [900, 300], tab2, font)
    gaston_button = pygame.Rect((w - 300), 10, 300, 300)
    gaston_surf = pygame.Surface(gaston_button.size)
    #noel
    noel = Character("assets/enemies/full_noel.png",
                     "assets/enemies/head_noel.png", [900, 300], tab2, font)
    noel_button = pygame.Rect((w - 300), (h - 300), 300, 300)
    noel_surf = pygame.Surface(noel_button.size)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if clodo_button.collidepoint(event.pos):
                        print("clodo")
                    if titi_button.collidepoint(event.pos):
                        print("titi")
                    if gaston_button.collidepoint(event.pos):
                        print("gaston")
                    if ronald_button.collidepoint(event.pos):
                        print("ronlald")
                    if maman_button.collidepoint(event.pos):
                        print("maman")
                    if noel_button.collidepoint(event.pos):
                        print("noel")
        surface.fill((255, 255, 255))                   #BACK
        clodo.setLogoPos(10, 10)                        #CLODO
        titi.setLogoPos(((w - 300) / 2), 10)            #TITI
        gaston.setLogoPos((w - 300), 10)                #GASTON
        ronald.setLogoPos(10, (h - 300))                #RONALD
        maman.setLogoPos(((w - 300) / 2), (h - 300))    #MAMAN
        noel.setLogoPos((w - 300), (h - 300))           #NOEL
        surface.blit(clodo.headSprite, clodo.logorect)
        surface.blit(titi.headSprite, titi.logorect)
        surface.blit(gaston.headSprite, gaston.logorect)
        surface.blit(ronald.headSprite, ronald.logorect)
        surface.blit(maman.headSprite, maman.logorect)
        surface.blit(noel.headSprite, noel.logorect)
        pygame.display.flip()

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

    pygame.mixer.music.load("assets/Music/main_theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.0)

    menu = pygame_menu.Menu('LA JOUTE', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', choose_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
