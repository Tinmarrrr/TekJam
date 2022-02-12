##
## EPITECH PROJECT, 2022
## Battle
## File description:
## Battle
##

import json
from src.Player import Player

def parseJson(level):
    file = 'Levels/Level' + str(level) + '.json'
    f = open(file)
    data = json.load(f)

    playerText = []
    enemyText = []

    for elem in data['player']:
        playerText.append(elem['Turn'])
    for elem in data['enemy']:
        enemyText.append(elem['Turn'])
    return [playerText, enemyText]

def battle(level):
    texts = parseJson(level)
    texts[0]