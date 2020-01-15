import nltk
from nltk.corpus import words
letters = input("Please choose 9 letters: \n")
def longestword(letters):
    longest_word = []
    n = 9
    while bool(longest_word) == False:
        longest_word = [w for w in nltk.corpus.words.words() if len(w) == n and nltk.FreqDist(w) <= nltk.FreqDist(letters)]
        n -= 1
    return longest_word
def backup(letters):
    n = len(longestword(letters)[0]) - 1
    second_longest = [w for w in nltk.corpus.words.words() if len(w) == n and nltk.FreqDist(w) <= nltk.FreqDist(letters)]
    while bool(second_longest) == False:
        n -= 1
        second_longest = [w for w in nltk.corpus.words.words() if len(w) == n and nltk.FreqDist(w) <= nltk.FreqDist(letters)]
    return second_longest
def countdown(letters):
    longest = longestword(letters)
    secondlongest = backup(letters)
    print("The best words are: " + str(longest))
    print("The next best words are: " + str(secondlongest))
longestword(letters)
backup(letters)
countdown(letters)
