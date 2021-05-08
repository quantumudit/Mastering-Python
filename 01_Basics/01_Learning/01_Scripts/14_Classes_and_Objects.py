
class Enemy:
    AttackLow = 60
    AttackHigh = 80

    def getAttack(self):
        print(self.AttackLow)


Enemy1 = Enemy()
Enemy1.getAttack()

Enemy2 = Enemy()
Enemy2.getAttack()

# "Self" is the short-cut way to refer to the current object
