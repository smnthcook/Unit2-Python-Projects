'''
WordCount
Samantha Cook
4/17/2023
Python II
'''

def word_count(word):
    '''
    Counts the number of words in a sentence
    '''
    count = len(word.split())
    return count

repeat = "y"
while repeat == "y":

    words = input("Enter a sentence >> ")
    print("There are", word_count(words), "words in this sentence.")
    repeat = input("Would you like to repeat? (y/n) >> ").lower()
    
    