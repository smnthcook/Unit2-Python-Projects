'''
ReverseWord
Samantha Cook
3/27/2023
Python II
'''

word = input("Enter a word >> ")
for i in range(len(word) - 1, -1, - 1):
    print(word[i], end="")