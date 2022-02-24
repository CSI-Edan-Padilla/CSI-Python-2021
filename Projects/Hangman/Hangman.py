import json, ssl
import random
import urllib. request
from randomname import Name 

def getWord():

    nameURL = "https://random-data-api.com/api/name/random_name"

    request = urllib.request.Request(nameURL)

    requestURL = json.loads(urllib.request.urlopen(request))

    current_name = Name(**requestURL)

    return current_name.name


steps = ["""
        __________________
        |                 |
        |                 |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |                 🎽
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |                 🎽🤳
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |                   🦿
        |
        |
        |
        |
        |
        |
        """,
        """
        __________________
        |                 |
        |                 |
        |                 😵
        |               💪🏿🎽🤳
        |                 🍆
        |                🦵🏽 🦿
        |
        |
        |
        |
        |
        |
        """]

print(steps[0])

wrong_numbers = ["0","1","2","3","4","5","6","7","8","9"]
wrong_symbols = ["`","~","!","@","#","$","%","^","&","*","(",")","_","-","+","=","{","}","[","]","\\","|",":",";","'","<",">",",",".","?","/"]
attemptedletters = []

def getInput():
    while(True):
        letter =  input( "Try to find the word to win the game of Hangman by finding the letters: " )

        if (len,(letter) !=1):
            continue 

        if letter in wrong_symbols:
            print("Wrong, you are bad 👎🏽")
            continue 

        if letter in wrong_symbols:
            print("Again, why are you bad?😐")
            continue 

        if letter in attemptedletters:
            print("Bad 💩")
            continue 

        attemptedletters.append(letter)
        return letter


def printword():
    temp:str=""
    for letter in Name:
        if letter in Name:
            print(letter)
            letter in attemptedletters
    if letter not in attemptedletters:
        temp +="_"
    else:
        temp += letter
    return temp


while True:
    print(steps[0])
    getInput()
    print()
    



