"""Drawing forests in a loop."""

__author__ = "730394272"

emoji: str = '\U0001F332'
depth: str = input("Depth: ")
t: str = emoji
if int(depth) < 1:
    print(" ")
else:
    total: int = int(depth)
    i: int = 1 
    print(t)
    while i < total:
        t = t + emoji
        print(t)
        i = i + 1
