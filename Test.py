import random

Player1 = False
Player2 = False

def Method():
    Turn = random.randrange(0, 10)
    if 0 <= Turn <= 5:
        Player1 = True
        print("Player 1 Starts.")
    elif 6 <= Turn <= 10:
        print("Player 2 Starts." )

Method()
