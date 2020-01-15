import nltk
from nltk.corpus import words
letters = input("Please enter the nine letters: \n")
def teatimeteaser(letters):
    word = [w for w in nltk.corpus.words.words() if nltk.FreqDist(w) == nltk.FreqDist(letters)]
    print(word)
    return word
teatimeteaser(letters)
