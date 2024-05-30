#Program to determine the likely-hood of  scratching off a $20,000 winner
#This is designed around the ALC lottery ticket
#Written by Chris Higgins

#Imports
import random

#Function for getting words
def GetWords(Count):
    WordList = []
    WordsChosen = []

    Dictionary = open("Libraries\Dictionary.txt", "r")
    for Word in Dictionary:
        WordList.append(Word.strip())
    Dictionary.close()

    for i in range(0, Count):
        WordsChosen.append(WordList[random.randint(0, len(WordList) - 1)])

    return WordsChosen
