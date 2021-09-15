"""Finding duplicate letters in a word."""

__author__ = "730394272"

word: str = input("Enter a word: ")
dup: bool = False
i: int = 0
while i < len(word):
    char = word[i]
    j: int = i + 1
    i = i + 1
    while j < len(word):
        dup: bool = (char == word[j]) or dup
        j = j + 1

print("Found duplicate: " + str(dup))