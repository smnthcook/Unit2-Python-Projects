'''
Palindrome
Samantha Cook
4/4/2023
Python II
'''


def isPalindrome(str):
'''
Checks if the word is a palidrome.
'''
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True


word = input("Enter a word >> ")
ans = isPalindrome(word)

if (ans):
    print("That is a palindrome.")
else:
    print("That is not a palindrome.")
