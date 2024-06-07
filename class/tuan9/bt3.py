# char = {
#     'Name': 'Light',
#     'Age': 17,
#     'Strength': 8,
#     'Defense': 10,
#     'HP': 100,
#     'Backpack': 'Shield, Bread Loaf',
#     'Gold': 100,
#     'Level': 2,
# }
# char.update({"Gold": char['Gold']+50})

# char.update({'Backpack':char['Backpack']+(', FlintStone')})

# char['Pocket'] = 'MonsterDex, Flashlight'
# print(char)

character = {
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP": 100,
    "Backpack": ["Shield", "Bread Loaf"], #tao mang de them append
    "Gold": 100,
    "Level": 2
}
#1
character["Gold"] += 50
#2
character["Backpack"].append("FlintStone")
#3
character["Pocket"] = ["MonsterDex", "Flashlight"]
print(character)