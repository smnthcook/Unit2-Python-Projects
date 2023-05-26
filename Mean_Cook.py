'''
Mean
Samantha Cook
4/4/2023
Python II
'''

def mean(numbers):
    
    amount_of_numbers = len(numbers)
    total = 0
    for number in numbers:
        total = total + number 
    return total / amount_of_numbers 



repeat = "y"
numbers = []
while repeat == "y":
    number = int(input("Enter a number >> "))
    numbers.append(number)
    repeat = input("Would you like to enter another number? (y/n) >> ")
    
print("The mean is:", mean(numbers))