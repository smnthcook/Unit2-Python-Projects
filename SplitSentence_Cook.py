'''
Split Sentence
Samantha Cook
3/27/2023
Python II
'''

sentence = input("Enter a complete sentence >> ")
start = 0
for i in range (0, len(sentence)):
    if sentence[i] == " " or sentence[i] == ".":
        print(sentence[start:i])
        start = i + 1