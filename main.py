import random
import string
from words import words

def getword(words):
    word=random.choice(words)    #randomly choose words

    while "-" in word or " "in word:
        word=random.choice(words)
    return word.upper()


def hangman():
    word=getword(words)
    letters = set(word)
    alpha=set(string.ascii_uppercase)
    guessed=set()

    print(letters)
    

    while len(letters)>0:
        show = [letter if letter in guessed else "-" for letter in word]
        print(" ".join(show))  
        print("You have guessed: "," ".join(guessed))
        guess=input("Enter the alphabet:").upper()
        if guess in alpha - guessed:
            guessed.add(guess)
            if guess in letters:  
                letters.remove(guess)
                print(letters)

        elif guess in guessed:
            print("Already guessed") 
        
        else:
            print("Invalid")
           
hangman()
