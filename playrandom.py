from common import *
from board import Board


def playrandom(game):
    """
    Plays a game where the computer always picks a random move.
    Updates game.result with the result
    :param game: the game being played
    :return: nothing
    """
    # keep playing a move until there's a result
    while game.result == -1:
        # if human turn
        if (game.first + game.turn) % 2 == 1:
            move = get_human_move(game)
            game.update_board(move)
            if game.check_for_win():
                # if True, human wins
                game.result = 0

        # else computer's turn
        else:
            move = get_random_move(game)
            computer_move_text(game)
            game.update_board(move)
            if game.check_for_win():
                # if True, computer wins
                game.result = 1

        printboard(game.cleanboard)

        # Check if board full and no result
        if game.turn == 10 and game.result == -1:
            game.result = 2
            break







