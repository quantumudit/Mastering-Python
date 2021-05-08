

from Classes.Game import Person, bcolors

Magic = [
    {"Name": "Fire", "Cost": 10, "Damage": 60},
    {"Name": "Thunder", "Cost": 10, "Damage": 60},
    {"Name": "Blizzard", "Cost": 10, "Damage": 60}
    ]

player = Person(460, 65, 60, 34, Magic)

print(player.GenerateDamage())
print(player.GenerateDamage())
print(player.GenerateDamage())

print(player.GenerateSpellDamage(0))
print(player.GenerateSpellDamage(1))