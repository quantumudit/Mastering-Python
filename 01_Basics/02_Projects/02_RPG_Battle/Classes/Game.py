
# Importing Necessary Libraries

import random

# Defining the classes:

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, HP, MP, Attack, Defense, Magic):
        self.MaxHP = HP
        self.HP = HP
        self.MinHP = MP
        self.MP = MP
        self.AttackHigh = Attack + 10
        self.AttackLow = Attack - 10
        self.Magic = Magic
        self.Actions = ["Attack", "Magic"]

    def GenerateDamage(self):
        return random.randrange(self.AttackLow, self.AttackHigh)

    def GenerateSpellDamage(self, i):
        MagicLow = self.Magic[i]["Damage"] - 5
        MagicHigh = self.Magic[i]["Damage"] + 5
        return random.randrange(MagicLow, MagicHigh)

    def TakeDamage(self, Damage):
        self.HP = self.HP - Damage

        if self.HP < 0:
            self.HP = 0
        return self.HP

    def GetHP(self):
        return self.HP

    def GetMaxHP(self):
        return self.MaxHP
    
    def GetMP(self):
        return self.MP