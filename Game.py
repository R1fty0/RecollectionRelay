import pygame
import random
# import os


class Color:
    def __init__(self, name, color):  # Constructor
        self.name = name
        self.color = color  # Tuple containing Color RGB Values

    def GetColor(self):
        return self.color


class Card:
    def __init__(self, name, frontImage, backImage):  # Constructor
        self.name = name
        self.frontImage = frontImage
        self.backImage = backImage


"""
    Colors
"""
Player1Color = Color("VividBurgundy", (164,  36,  59))
Player2Color = Color("BlueNCS", (46, 134, 172))
BoardColor = Color("Ecru", (216, 201, 155))
CardBackColor = Color("HarvestGold", (216, 151, 60))
CardFront = Color("AlloyOrange", (189, 199, 47))    # Also is Board Outline
CardOutlineColor = Color("White", (255, 255, 255))
"""
    Window Stats
"""
# Frames Per Second
FPS = 75  # My monitor's Refresh Rate, change it to what you would like.

# Width and Height of the Window
WindowWidth, WindowHeight = 800, 600

# Creates Game Window
Window = pygame.display.set_mode((WindowWidth, WindowHeight))  # dimensions for Width & Height of Window

# Window Name
pygame.display.set_caption("Recollection Relay")


"""
    Main Game Loop and Mechanics
"""
# Turn States - Which Player's Turn it is:
Player1Turn = False
Player2Turn = False


def Graphics():   # Draws all visuals on screen
    if Player1Turn:
        Window.fill(Player1Color.GetColor())
    elif Player2Turn:
        Window.fill(Player2Color.GetColor())

    pygame.display.update()  # Updates the Screen with what was drawn.


def DecideStartingPlayer():  # randomly decides which player starts first
    Turn = random.randrange(0, 10)
    if 0 <= Turn <= 5:   # player 1 starts first
        global Player1Turn
        Player1Turn = True

    elif 6 <= Turn <= 10:  # player 2 starts first
        global Player2Turn
        Player2Turn = True


def Run():  # Basically the Unity Update Method - all code runs here.

    DecideStartingPlayer()  # Decides Which Player Starts

    GameClock = pygame.time.Clock()  # Clock that maintains FPS

    IsGameRunning = True  # If this boolean is true, then the program runs.

    while IsGameRunning:  # Main Game Loop - code runs here
        GameClock.tick(FPS)  # Runs the Game at the Desired FPS

        for event in pygame.event.get():  # Quits Program if the X button is pressed
            if event.type == pygame.QUIT:
                IsGameRunning = False
        Graphics()
    pygame.quit()  # Quits program


if __name__ == "__main__":  # Program Starts Here
    Run()
