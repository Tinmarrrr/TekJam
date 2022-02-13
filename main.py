import pygame
import pygame_menu

from src.character import Character
from src.Battle import battle
from src.InfosBattle import InfosBattle

WIDTH = 1280
HEIGHT = 720

def choose_menu():
    gorille = Character("assets/gorilla/gorilla_base.png", "assets/gorilla/gorilla_base.png", [100, 300], tab1, font)
    clodo = Character("assets/enemies/full_clodo.png", "assets/enemies/head_clodo.png", [900, 300], tab2, font)
    titi = Character("assets/enemies/full_titi.png", "assets/enemies/head_titi.png", [900, 300], tab2, font)
    ronald = Character("assets/enemies/full_ronald.png", "assets/enemies/head_ronald.png", [900, 300], tab2, font)
    maman = Character("assets/enemies/full_maman_enfant.png", "assets/enemies/head_maman_enfant.png", [900, 300], tab2, font)
    gaston = Character("assets/enemies/full_gaston.png", "assets/enemies/head_gaston.png", [900, 300], tab2, font)
    noel = Character("assets/enemies/full_noel.png", "assets/enemies/head_noel.png", [900, 300], tab2, font)


    w, h = pygame.display.get_surface().get_size()
    running = True
    start = False
    lvl = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    start = True
        surface.fill((255, 255, 255))

        clodo.setLogoPos(10, 10) #1
        gaston.setLogoPos(((w - 300) / 2), 10) #2
        titi.setLogoPos(((w - 300) / 1), 10) #3

        ronald.setLogoPos((10), ((h - 300) / 1)) #4
        maman.setLogoPos(((w - 300) / 2), ((h - 300) / 1)) #5
        noel.setLogoPos((w - 300), (h - 300)) #6

        if start == False:
            surface.blit(clodo.headSprite, clodo.logorect)
            surface.blit(titi.headSprite, titi.logorect)
            surface.blit(gaston.headSprite, gaston.logorect)
            surface.blit(ronald.headSprite, ronald.logorect)
            surface.blit(maman.headSprite, maman.logorect)
            surface.blit(noel.headSprite, noel.logorect)
        else:
            infosBt = InfosBattle()
            if battle(surface, infosBt.loadJson(lvl), font, 0) == False:
                running = False
        pygame.display.flip()


# def start_the_game():

#     running = True
#     while running:

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     gorille.nextText()
#                 if event.key == pygame.K_RIGHT:
#                     clodo.nextText()

#         surface.fill((255, 255, 255))
#         surface.blit(gorille.sprite, gorille.rect)
#         surface.blit(clodo.sprite, clodo.rect)
#         surface.blit(gorille.currentText, (200, 200))
#         surface.blit(clodo.currentText, (800, 200))

#         pygame.display.flip()


def initMusic():
    pygame.mixer.music.load("assets/Music/main_theme.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.0)

def initMenu():
    menu = pygame_menu.Menu('LA JOUTE', WIDTH, HEIGHT,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.button('Play', choose_menu)
    menu.add.button('Quit', pygame_menu.events.EXIT)
    return menu

if __name__ == '__main__':
    pygame.init()

    pygame.font.init()
    font = pygame.font.SysFont('Arial', 20)
    surface = pygame.display.set_mode((WIDTH, HEIGHT))

    tab1 = [" ", " "]
    tab2 = [" ", " "]

    initMusic()
    menu = initMenu()

    menu.mainloop(surface)
