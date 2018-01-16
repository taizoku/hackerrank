from .classes.enemy import Enemy

import random


enemy = Enemy(200, 60)
print("HP:", enemy.get_hp())

'''
class Enemy:
    hp = 200

    def __init__(self, lowAttack, hiAttack):
        self.lowAttack = lowAttack
        self.hiAttack = hiAttack

    def get_attack(self):
        print("Base damage is:", self.lowAttack)

    def get_hp(self):
        print("HP is: ", self.hp)


enemy1 = Enemy(10, 15)
enemy1.get_attack()
enemy1.get_hp()

enemy2 = Enemy(1, 5)
enemy2.get_attack()
enemy2.get_hp()
'''
