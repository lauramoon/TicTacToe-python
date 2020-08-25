from common import *
from board import Board

def playrandom(game):
    if game.first == 0:
        # if human goes first
        get_human_move(game)

        for i in range(0,4):
            # moves 2-9
            play_random_move(game)
            if game.check_for_win():
                game.result = 1  # computer
                break

            get_human_move(game)
            if game.check_for_win():
                game.result = 0  # human wins
                break

    else:
        play_random_move(game) # move 1

        for i in range(0,4):
            # moves 2-9
            get_human_move(game)
            if game.check_for_win() == True:
                game.result = 0  # human wins
                break

            play_random_move(game)
            if game.check_for_win() == True:
                game.result = 1  # computer wins
                break

    # if all 9 turns complete without win, the game is a draw
    if game.result == -1:
        game.result = 2






