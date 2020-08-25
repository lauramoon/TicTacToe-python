from common import *
from board import Board


def play_chosen_move(game, move):
    input("Press 'Enter' to have the computer play")
    print("")
    print("Computer plays: ")
    game.record[game.turn] = move
    game.updateboards(0)
    printboard(game.cleanboard)


def playcasual(game):
    if game.first == 0:
        # if human goes first, moves 1-3:
        get_human_move(game)
        play_random_move(game)
        get_human_move(game)

        for i in range(0, 3):
            # moves 4 - 9
            # after move 3, on computer's turn,
            # need to check if AI can win then if human can win
            winner = game.find_winner()
            block = game.find_block()
            if winner != 0:
                play_chosen_move(game, winner)
                game.result = 1
                break
            elif block != 0:
                # play block move
                play_chosen_move(game, block)
            else:
                play_random_move(game)

            get_human_move(game)
            if game.check_for_win():
                game.result = 0  # human wins
                break

    else:
        # computer goes first
        # first 4 moves
        for i in range(0, 2):
            play_random_move(game)
            get_human_move(game)
        
        # moves 5-8, have to check for blocking move, then for winning move
        for i in range(0, 2):
            winner = game.find_winner()
            block = game.find_block()
            if winner != 0:
                play_chosen_move(game, winner)
                game.result = 1
                break
            elif block != 0:
                # play block move
                play_chosen_move(game, block)
            else:
                play_random_move(game)

            get_human_move(game)
            if game.check_for_win():
                game.result = 0  # human wins
                break
    
        # only one choice for computer's last move, check if there's a result first
        if game.result == -1:
            move = int(max(game.moves))
            play_chosen_move(game, move)
            if game.check_for_win():
                # AI wins
                game.result = 1
            else:
                # Game is a draw
                game.result = 2


