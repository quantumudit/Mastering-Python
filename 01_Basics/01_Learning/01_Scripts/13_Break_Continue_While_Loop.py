import random

PlayerHP = 260
EnemyAttackLow = 60
EnemyAttackHigh = 80

while PlayerHP > 0:
    PlayerDamage = random.randrange(EnemyAttackLow, EnemyAttackHigh)
    PlayerHP = PlayerHP - PlayerDamage

    if PlayerHP <= 30:
        PlayerHP = 30

    print("Enemy Strikes for", PlayerDamage,
          "Points of Damage. Current HP is: ", PlayerHP)

    if PlayerHP > 30:
        continue

    if PlayerHP == 30:
        print("You've low health and you've been teleported to the nearest inn.")
        break
