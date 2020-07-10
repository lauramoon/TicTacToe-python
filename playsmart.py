from common import *
from board import Board
from playbook import Playbook

def get_AI_move(game):
    # Determine next AI move and show it on board
    next = input("Press 'Enter' to have the computer play")
    print("")
    print("Computer plays:")

    if game.turn == 2:
        # If human played in middle, play in top left, else play in middle
        if game.trecord[1] == 5:
            game.trecord[2] = 1
        else:
            game.trecord[2] = 5

    elif game.turn == 3:
        # always play in upper right on transformed board
        game.trecord[3] = 3

    else:
        # for moves 4-9, look up next move
        nextmove = Playbook(game.key).getresult()
        game.trecord[game.turn] = nextmove[0]
        game.result = nextmove[1]
    
    # update board with AI move
    game.updateboards(1)
    # print("record", game.record)
    # print("trecord", game.trecord)
    # print("rotation", game.rotate)
    # print("flip", game.flip)
    printboard(game.cleanboard)


def playsmart(game):
    # run through up to nine moves using above method to get AI moves
    if game.first == 0:
        #if human is first
        get_human_move(game)

        for i in range(0, 4):
            # get moves 2-9, first computer, then human
            get_AI_move(game)

            if game.result != -1:
                break

            get_human_move(game)

        # if loop completed, game is a draw
        game.result = 2

    else:
        # If computer goes first, play in middle for first move
        game.trecord[1] = 5
        game.updateboards(1)
        print("Computer plays:")
        printboard(game.cleanboard)

        for i in range(0,4):
            get_human_move(game)

            get_AI_move(game)
            if game.result != -1:
                break


