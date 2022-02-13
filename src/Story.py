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

def storyPannel(surface, monkeyImg, enemyImg, text):
    surface.fill((255, 255, 255))
    enemyText = textBox(surface, 200, 500, text)
    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                return True
        pygame.display.update()