import random


class Enemy:
    def __init__(self, lowAttack, hiAttack):
        self.lowAttack = lowAttack
        self.hiAttack = hiAttack

    def get_attack(self):
        print("Base damage is:", self.lowAttack)


enemy1 = Enemy(10, 15)
enemy1.get_attack()