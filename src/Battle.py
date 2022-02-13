from distutils.log import info
import pygame
from src.Button import *
from src.InfosBattle import *

def battle(surface, level):
    infosBt = InfosBattle()
    infosBt.loadJson(level)

    surface.fill((255, 255, 255))
    shout = infosBt.enemy.middleShout
    confidence = 0
    for turn in infosBt.turns:
        running = True
        enemyText = EnemyTextBox(surface, 1280, 0, infosBt.enemy.name + ": " + shout)
        enemyPunch = EnemyTextBox(surface, 1280, 100, turn.punch)
        b1 = Button(surface, 80, 630, turn.responses[0].sentence)
        b2 = Button(surface, 700, 630, turn.responses[1].sentence)
        b3 = Button(surface, 80, 680, turn.responses[2].sentence)
        b4 = Button(surface, 700, 680, turn.responses[3].sentence)
        while running:
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    return False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[0].value
                        running = False
                    if b2.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[1].value
                        running = False
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[2].value
                        running = False
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[3].value
                        running = False
            pygame.display.update()


    # text1 = font.render(answers[0][turn]["Choice 1"], False, (0, 0, 0))
    # text2 = font.render(answers[0][turn]["Choice 2"], False, (0, 0, 0))
    # text3 = font.render(answers[0][turn]["Choice 3"], False, (0, 0, 0))
    # text4 = font.render(answers[1][turn]["Answer"], False, (0, 0, 0))

    # surface.blit(text1, (200, 100))
    # surface.blit(text2, (200, 200))
    # surface.blit(text3, (200, 300))
    # surface.blit(text4, (200, 400))