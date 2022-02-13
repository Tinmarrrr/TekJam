from distutils.log import info
import pygame
from src.Button import *
from src.InfosBattle import *
from src.character import Character
from src.Story import storyPannel

def getEnemyResponse(value, infosBt):
    if value < 0:
        return infosBt.enemy.winShout
    elif value > 0:
        return infosBt.enemy.looseShout
    else:
        return infosBt.enemy.middleShout

def battle(surface, level, player, enemy):
    infosBt = InfosBattle()
    infosBt.loadJson(level)

    shout = infosBt.enemy.middleShout
    confidence = 0
    storyPannel(surface, player, enemy, infosBt.enemy.description)
    player.setScale()
    enemy.setScale()
    for turn in infosBt.turns:
        surface.fill((255, 255, 255))
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
                        shout = getEnemyResponse(turn.responses[0].value, infosBt)
                        running = False
                    if b2.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[1].value
                        shout = getEnemyResponse(turn.responses[1].value, infosBt)
                        running = False
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[2].value
                        shout = getEnemyResponse(turn.responses[2].value, infosBt)
                        running = False
                    if b4.collidepoint(pygame.mouse.get_pos()):
                        confidence += turn.responses[3].value
                        shout = getEnemyResponse(turn.responses[3].value, infosBt)
                        running = False
            surface.blit(player.sprite, player.rect)
            surface.blit(enemy.sprite, enemy.rect)
            pygame.display.update()
    if confidence < 0:
        resultBattle = "You loose agains " + infosBt.enemy.name
    elif confidence >= 2:
        resultBattle = "You win against " + infosBt.enemy.name
    else:
        resultBattle = "You pass against " + infosBt.enemy.name
    storyPannel(surface, player, enemy, resultBattle)
    return True