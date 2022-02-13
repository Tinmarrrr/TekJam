import pygame

def battle(surface, answers, font, turn):
    print(answers[1][1]["Answer"])
    text1 = font.render(answers[0][turn]["Choice 1"], False, (0, 0, 0))
    text2 = font.render(answers[0][turn]["Choice 2"], False, (0, 0, 0))
    text3 = font.render(answers[0][turn]["Choice 3"], False, (0, 0, 0))
    text4 = font.render(answers[1][turn]["Answer"], False, (0, 0, 0))

    surface.blit(text1, (200, 100))
    surface.blit(text2, (200, 200))
    surface.blit(text3, (200, 300))
    surface.blit(text4, (200, 400))