##
## EPITECH PROJECT, 2022
## Enemy
## File description:
## Enemy
##

class Enemy:
    hp = 15
    damages = 5
    question = 0
    def __init__(self, lvl):
        self.damages = self.damages + 1.5 * lvl
    def takeDamages(self, EnemyDamages):
        self.hp = self.hp - EnemyDamages
    def dealDamages(self, player):
        player.takeDamages(self.damages)
         