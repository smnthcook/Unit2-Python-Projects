'''
RandomNamePicker
Samantha Cook
4/4/2023
Python II
'''
import random

names = []
name = input("Enter a name (1 to stop) >> ")
while name != "1":
    names.append(name)
    name = input("Enter a name (1 to stop) >>")
if len(names) > 0:
    print("I pick", random.choice(names))
else:
    print("Invalid! No names were entered.")