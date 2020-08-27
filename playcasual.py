from common import *


def play_casual(game):
    """
    plays a casual game, where the computer plays a random move
    unless it can play a winning move or block the human from winning
    updates game.result with the result
    :param game: the game being played
    :return: none
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
            # get winning and blocking moves, if exist
            winner = game.find_winner()
            block = game.find_block()
            # set move to winning move, if exists
            if winner != 0:
                move = winner
                # and set result
                game.result = 1
            # check for blocking move and set if exists
            elif block != 0:
                move = block
            # otherwise get random move
            else:
                move = get_random_move(game)

            # show text for computer move and update game record
            computer_move_text(game)
            game.update_board(move)

        print_board(game.clean_board)

        # Check if board full and no result
        if game.turn == 10 and game.result == -1:
            game.result = 2
            break


