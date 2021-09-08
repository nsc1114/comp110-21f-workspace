"""Counting letters in a string."""

__author__ = "730394272"


letter: str = input("What letter do you want to search for?")
word: str = input("Enter a word:")
count: int = 0
index: int = 0
while index < len(word):
    if letter == word[index]:
        count = count + 1
        index = index + 1
    else: 
        index = index + 1

print("Count: " + str(count))

