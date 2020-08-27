""" functions used by various modules"""


def print_board(b):
    """
    prints tic tac toe board to screen
    :param b: list of symbols or numbers to put in boxes, starting upper left, by rows
    :return: nothing
    """
    white_space_big = "        |     |     "
    small_space = "  |  "
    line = "   -----|-----|-----"

    print("")
    print(white_space_big)
    print("     " + b[1] + small_space + b[2] + small_space + b[3])
    print(white_space_big)
    print(line)
    print(white_space_big)
    print("     " + b[4] + small_space + b[5] + small_space + b[6])
    print(white_space_big)
    print(line)
    print(white_space_big)
    print("     " + b[7] + small_space + b[8] + small_space + b[9])
    print(white_space_big)
    print("")


def get_human_move(game):
    """
    Gets the human player's next move
    :param game: game being played
    :return: number representing location of next move
    """
    # Turn 1 gets slightly different question
    if game.turn == 1:
        print_board(game.num_board)

        move = input("Where do you play first? ")
        while move not in game.moves:
            move = input("Where do you play first? Enter the number for the location: ")
        move = int(move)

    # no need to ask for ninth move, as only one choice left
    elif game.turn == 9:
        move = int(max(game.moves))
        print("There is only one place left to play")
        input("Press 'Enter' to see your last move")

    else:
        symbol = game.turn_mark[game.turn]

        input("Press 'Enter' to pick your next move")
        print_board(game.num_board)
        print("You are playing " + symbol)
        move = " "

        while move not in game.moves:
            move = input("Enter your next move location: ")

        move = int(move)
        # game.record[game.turn] = move

    return move


def get_random_move(game):
    """
    Takes a game board and returns valid random move
    :param game: the game being played
    :return: valid random move from the set of moves remaining
    """
    move = int(game.moves.pop())
    return move


def computer_move_text(game):
    """
    Prompts human to press enter when ready to see computer's next move,
    headlines the board with the computer's move
    :param game:
    :return: nothing
    """
    if game.turn != 1:
        input("Press 'Enter' to have the computer play")
        print("")
    print("Computer plays: ")
