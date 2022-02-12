##
## EPITECH PROJECT, 2022
## player
## File description:
## Player
##

class Player:
    hp = 15
    lvl = 0
    question = 0
    damages = 6
    def takeDamages(self, damages):
        self.hp = self.hp - damages
    def getPossibleAnswers():
        return 0
    def dealDamages(self, enemy):
        enemy.takeDamages(self.damages + self.lvl)
    