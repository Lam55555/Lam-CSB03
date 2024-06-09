# 1
# pc = {
#     'HP': 20,
#     'DELL': 50,
#     'MACBOOK': 12,
#     'ASUS': 30,
# }

# print(f"Available Macbooks: {pc['MACBOOK']}")
# name = input('Input a brand: ')
# print(f"Available {name}s: {pc[name]}")

# 2.1-2.2

# pc["TOSHIBA"] = "10"
# brand = str(input('Input a brand: '))
# amount = int(input('Input a mount: '))
# pc[brand] = amount

# for i in pc:
#     print(f"- {i}: {pc[i]}")

# 2.3

# pc['DELL'] = 60
# pc['MACBOOK'] = 2

# for i in pc:
#     print(f"- {i}: {pc[i]}")

# 2.4

# tong = 0
# for i in pc.values():
#     tong+=i
# print('Total product:',tong)

# 3

# pcprice = {
#     'HP':600,
#     'DELL':650,
#     'MACBOOK':1200,
#     'ASUS':400
# }

# print(f"Price of Asus: {pcprice['ASUS']}")
# price = input('Input a brand: ')
# print(f"Price of {price}: {pcprice[price]}")

# 4.1
# print('Total price:',pcprice['ASUS']*5)

# 4.2

# brand = input('Input a brand: ')
# amountPc = int(input('Input amount to buy: '))
# print(f"Total price: {pcprice[brand]*amountPc}")

# 4.3
# brand = input('Input a brand: ')
# amountPc = int(input('Input amount to buy: '))
# print(f"Total price: {pcprice[brand]*amountPc}")

# print('Available product: ')
# if brand in pc:
#     pc[brand] = pc[brand] - amountPc
# for i in pc:
#     print(f"- {i}: {pc[i]}")

# 5
# hang  = {}
# print('Total price of avalable brand: ')
# for i in pcprice:
#     if i in pc:
#         hang[i] = pc[i]*pcprice[i]
# for i in hang:
#     print(f"-{i}: {hang[i]}")

# print('Total value of availabel items:',sum(hang.values()))

char = {
    'Name': 'Light',
    'Age': 17,
    'Strength': 8,
    'Defense': 10,
    'HP': 100,
    'Backpack': 'Shield, Bread Loaf',
    'Gold': 100,
    'Level': 2,
}
#6
# char['Gold']+=50
# print('Gold',char['Gold'])

# char.update({'Backpack':char['Backpack']+(', FlintStone')})
# print('Backpack:',char['Backpack'])


skill = {
  'Skill 1': [
    {'Name': 'Tackle', 'Minimum level': 1, 'Damage': 5, 'Hit rate': 0.3 },
  ],
  'Skill 2': [
    {'Name': 'Quick Attack','Minimum level': 2, 'Damage': 3, 'Hit rate': 0.5},
  ],
  'Skill 3':[
      {'Name': 'Strong Kick', 'Minimum level': 4, 'Damage': 9, 'Hit rate': 0.2}
  ]
}
# #7
# for i in skill:
#     for y in skill[i]:
#         print(f"{i}: {y['Name']}")












# Src: Tài
#8
# import random
# myChar = {
#     "Name": "Light",
#     "Age": 17,
#     "Strength": 8,
#     "Defense": 10,
#     "HP": 100,
#     "Backpack": [
#         "Shield", 
#         "Bread Loaf"
#         ],
#     "Gold": 100,
#     "Level": 2
# }
# mySkills = {
#     "Skill 1": {
#         "Index" : 1,
#         "Name": "Tackle", 
#         "Minimum level": 1,
#         "Damage": 5,
#         "Hit rate": 0.3
#         },
#     "Skill 2": {
#         "Index" : 2,
#         "Name": "Quick Attack",
#         "Minimum level": 2,
#         "Damage": 3,
#         "Hit rate": 0.5
#         },
#     "Skill 3": {
#         "Index" : 3,
#         "Name": "Strong Kick",
#         "Minimum level": 4,
#         "Damage": 9,
#         "Hit rate": 0.2
#         }
# }
# #Bai 1:
# for k,v in mySkills.items():
#     print("-",k,":",v["Name"])
# skill_num = int(input("Choose skill by number (1->3): "))
# for k,v in mySkills.items():
#     if v["Index"] == skill_num:
#         print("You chose",v["Name"])
#         if myChar["Level"] >= v["Minimum level"]:  ##Bai 2:
#             ran = random.random()         
#             # print(ran)
#             if ran < v["Hit rate"]:
#                 print("Damage:",v["Damage"])
#             else: print("Attack missed.")
#         else: print("Cannot deployed. Required level",v["Minimum level"])

