"""Repeating a beat in a loop."""

__author__ = "730394272"


beat: str = input("What beat do you want to repeat?")
num: str = input("How many times do you want to repeat it?")
total: str = beat
if int(num) == 0:
    print("No beat...")
else: 
    runtime: int = int(num)
    while runtime > 1: 
        total = total + " " + beat
        runtime = runtime - 1
    print(total)
