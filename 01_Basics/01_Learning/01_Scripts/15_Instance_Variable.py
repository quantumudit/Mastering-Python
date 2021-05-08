
class Enemy:

    HP = 200

    def __init__(self, AttackLow, AttackHigh):

        self.AttackLow = AttackLow
        self.AttackHigh = AttackHigh

    def getAttack(self):
        print(self.AttackLow)

    def getHP(self):
        print("HP is", self.HP)


Enemy1 = Enemy(40, 49)
Enemy1.getAttack()
Enemy1.getHP()

Enemy2 = Enemy(70, 79)
Enemy2.getAttack()
Enemy2.getHP()
