import pygame
from src.Button import *

def battle(surface, answers, font, turn):
    b1 = Button(surface, 80, 630, "Ta maman")
    b2 = Button(surface, 700, 630, "Ton papa")
    b3 = Button(surface, 80, 680, "Ton oncle")
    b4 = Button(surface, 700, 680, "Ta tante")
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    button1()
                if b2.collidepoint(pygame.mouse.get_pos()):
                    button2()
                if b3.collidepoint(pygame.mouse.get_pos()):
                    button3()
                if b4.collidepoint(pygame.mouse.get_pos()):
                    button4()
        pygame.display.update()


    # text1 = font.render(answers[0][turn]["Choice 1"], False, (0, 0, 0))
    # text2 = font.render(answers[0][turn]["Choice 2"], False, (0, 0, 0))
    # text3 = font.render(answers[0][turn]["Choice 3"], False, (0, 0, 0))
    # text4 = font.render(answers[1][turn]["Answer"], False, (0, 0, 0))

    # surface.blit(text1, (200, 100))
    # surface.blit(text2, (200, 200))
    # surface.blit(text3, (200, 300))
    # surface.blit(text4, (200, 400))