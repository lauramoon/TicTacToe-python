from board import Board
from common import printboard
from playsmart import playsmart
from playrandom import playrandom
from playcasual import playcasual


def playgame():
    print("Select the game mode:")
    print("1 - Random")
    print("2 - Casual")
    print("3 - Smart")
    selection = input()
    while selection not in ["1", "2", "3"]:
        selection = input("Please enter 1, 2, or 3: ")
    mode = int(selection)

    print("Who goes first?")
    print("0 - Human")
    print("1 - Computer")
    answer = input()
    while answer not in ["0", "1"]:
        answer = input("Please enter 0 or 1: ")
    first = int(answer)
    game = Board(first, mode)

    if mode == 1:
        playrandom(game)
    elif mode == 2:
        playcasual(game)
    else:
        playsmart(game)

    if game.result == 0:
        print("You win!")
    if game.result == 1:
        print("Computer wins!")
    if game.result == 2:
        print("The game is a draw.")
    print(" ")
    # printboard(game.cleanboard)

def main():
    print("You are playing Tic Tac Toe")
    playagain = True

    while playagain == True:
        playgame()
        again = " "
        while again not in ["Y", "y", "N", "n"]:
            again = input("Do you want to play again? (Y/N)")
        if again in ["N", "n"]:
            playagain = False

main()

