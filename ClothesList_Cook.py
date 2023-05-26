'''
ClothesList
Samantha Cook
3/31/2023
Python II
'''

clothes = []

clothing_item = input("Enter a piece of clothing (q to quit) >> ")
while clothing_item != "q":
    clothes.append(clothing_item)
    clothing_item = input("Enter a piece of clothing (q to quit) >> ")
    
for clothing_item in clothes:
    print(clothing_item)
    
