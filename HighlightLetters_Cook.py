'''
HighlightLetters
Samantha Cook
3/24/2023
Python II
'''
import colorama
word = input("Enter a five letter word >> ").strip()
if len(word) == 5:
    print(colorama.Fore.RED + word[0], end="")
    print(colorama.Fore.GREEN + word[1], end="")
    print(colorama.Fore.MAGENTA + word[2], end="")
    print(colorama.Fore.CYAN + word[3], end="")
    print(colorama.Fore.YELLOW + word[4], end="")
else:
    print("Invaild word! Must be five letters long.")