"""Coin-flipping Tourney"""

__author__ = "730394272"

from random import randint
winemoji: str = "\U00002728"
lemoji: str = "\U0001F625"
player: str = input("Enter player name: ")
points: int = 0


def greet() -> None:
    """Greets the player"""
    print(f"Welcome {player} to the ultimate coin flipping tournament. Can you reach 10 correct guesses in a row?")


def toss(points) -> int:
    coin: int = randint(1, 2)
    flip: str = input("Heads or tails or quit? ")
    if flip == "Quit":
        points = quit(points)
        points = -1
    else: 
        if coin == 1 and flip != "Quit":
            print("The coin lands on....HEADS")
        else:
            if coin == 2 and flip != "Quit":
                print("The coin lands on....TAILS")
        if coin == 1 and flip == "Heads":
            print(f"{winemoji}{winemoji}You win!!!!{winemoji}{winemoji}")
            points = points + 1
            print(f"Score: {points}")
        else:
            if coin == 1 and flip == "Tails":
                print(f"Sorry {player}, you lose. {lemoji}")
                print(f"Score: {points}")
                points = -1
        if coin == 2 and flip == "Tails":
            print(f"{winemoji}{winemoji}You win!!!!{winemoji}{winemoji}")
            points = points + 1
            print(f"Score: {points}")
        else:
            if coin == 2 and flip == "Heads":
                print(f"Sorry {player}, you lose. {lemoji}")
                print(f"Score: {points}")
                points = -1
        return points
        
            
def main() -> None:
    """Main"""
    points: int = 0
    while points == 0:
        greet()
        quit(points)
        while points >= 0 and points < 10: 
            points = toss(points)


def quit(points) -> int:
    flip: str = input("Heads or tails or quit? ")
    if flip == "Quit":
        print(f"Goodbye {player}! Here is your score: {points}")
        points = -1
    return points


main()