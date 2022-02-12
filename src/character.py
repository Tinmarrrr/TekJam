from email.mime import image
import pygame

class Character:

    def __init__(self, imagePath, position):
        self.sprite = pygame.image.load(imagePath)
        self.rect = self.sprite.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.setScale()

    def setScale(self, x = 220, y = 220):
        self.sprite = pygame.transform.scale(self.sprite, (x, y))

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y