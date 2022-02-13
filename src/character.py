import pygame

class Character:

    def __init__(self, imagePath, logoPath, position, texts, font):
        self.sprite = pygame.image.load(imagePath)
        self.headSprite = pygame.image.load(logoPath)
        self.rect = self.sprite.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.logorect = self.headSprite.get_rect()

        self.logorect.x = position[0]
        self.logorect.y = position[1]

        self.font = font
        self.texts = texts
        self.textIndex = 0
        self.currentText = self.font.render(texts[self.textIndex], False, (0, 0, 0))
        self.setScale()

    def setScale(self, x = 220, y = 220):
        self.sprite = pygame.transform.scale(self.sprite, (x, y))

    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y

    def setLogoPos(self, x, y):
        self.logorect.x = x;
        self.logorect.y = y;

    def nextText(self):
        self.textIndex += 1
        if self.textIndex >= len(self.texts):
            self.textIndex = 0
        self.currentText = self.font.render(self.texts[self.textIndex], False, (0, 0, 0))