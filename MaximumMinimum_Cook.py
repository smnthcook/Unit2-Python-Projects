'''
Maximum, Minimum
Samantha Cook
4/4/2023
Python II
'''



def maximum(numbers):
'''
Finds the max of the list of numbers.
'''
    max(numbers)
    return max(numbers)

def minimum(numbers):
'''
Finds the min of the list of numbers.
'''
    min(numbers)
    return min(numbers)


numbers = []
repeat = "y"
while repeat == "y":
    
    number = input("Enter a number >> ") 
    numbers.append(number)
    repeat = input("Would you like to enter another number (y/n) >> ")

print("Maximum:", maximum(numbers))
print("Minimum:", minimum(numbers))
