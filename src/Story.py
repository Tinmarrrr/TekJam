import pygame
from src.Button import *

def textBox(screen, positionX, positionY, text):
        screen = screen
        font = pygame.font.SysFont("Arial", 40)
        text_render = font.render(text, 1, (0, 0, 0))
        x, y, w , h = text_render.get_rect()
        x = positionX
        y = positionY
        return screen.blit(text_render, (x, y))

def storyPannel(surface, monkey, enemy, text):
    surface.fill((255, 255, 255))
    enemyText = applyBackLine(surface, 200, 500, text, 12)
    surface.blit(monkey.sprite, monkey.rect)
    surface.blit(enemy.sprite, enemy.rect)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.update()

def applyBackLine(screen, positionX, positionY, text, size):
    phrase = text
    font = pygame.font.SysFont("Arial", size)
    text_render = font.render(text, 1, (0, 0, 0))
    x, y, w , h = text_render.get_rect()
    x = positionX
    y = positionY
    bulle = text_render.get_rect()
    x,y = bulle.topleft
    for ligne in phrase.splitlines():
        x,y = screen.blit(font.render(ligne,1,(0,0,0)),(x,y)).bottomleft
    return screen

