##
## EPITECH PROJECT, 2022
## Battle
## File description:
## Battle
##

import json
from src.Enemy import Enemy
from src.Player import Player

def battle(Enemy, Player, Level):
    file = 'Levels/Level' + str(Level) + '.json'
    f = open(file)
    data = json.load(f)
    enemyText = []
    playerText = []
    for elem in data['player']:
        playerText.append(elem['Turn'])
    for elem in data['enemy']:
        enemyText.append(elem['Turn'])
    print(playerText[0])
    
