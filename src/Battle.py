from distutils.log import info
import pygame
from src.Button import *
from src.InfosBattle import *
from src.character import Character

def battle(surface, level, player, enemy):
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
            surface.blit(player.sprite, player.rect)
            surface.blit(enemy.sprite, enemy.rect)
            pygame.display.update()