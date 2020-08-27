from board import Board
from playsmart import play_smart
from playrandom import play_random
from playcasual import play_casual


def play_game():
    """
    One play-through of a game of tic-tac-toe.
    :return:
    """
    # Player picks game mode
    print("Select the game mode:")
    print("1 - Random")
    print("2 - Casual")
    print("3 - Smart")
    selection = input()
    while selection not in ["1", "2", "3"]:
        selection = input("Please enter 1, 2, or 3: ")
    mode = int(selection)

    # Player picks if player or human goes first
    # could add random option
    print("Who goes first?")
    print("0 - Human")
    print("1 - Computer")
    answer = input()
    while answer not in ["0", "1"]:
        answer = input("Please enter 0 or 1: ")
    first = int(answer)

    # Create the game board
    game = Board(first, mode)

    # Play game according to selected game mode
    if mode == 1:
        play_random(game)
    if mode == 2:
        play_casual(game)
    if mode == 3:
        play_smart(game)

    # Report game result to the player
    # could return result to main and keep a tally of results there
    result_messages = ("You win!", "Computer wins!", "The game is a draw.")
    print(result_messages[game.result])
    print(" ")


def main():
    """
    Game wrapper function. Run this to run the game.
    Stops when player doesn't want to play again.
    :return: nothing
    """
    print("You are playing Tic Tac Toe")
    play_again = True

    # keep playing game until player decides not to play again
    while play_again:
        # single game play
        play_game()
        again = " "
        while again not in ["Y", "N"]:
            again = input("Do you want to play again? (Y/N)").upper()
        if again == "N":
            play_again = False


main()
