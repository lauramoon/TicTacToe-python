import time

def printboard(b):
    # prints a board to screen
    wsbig = "        |     |     "
    wssm = " | "
    line = "   -----|-----|-----"

    print("")
    print(wsbig)
    print("    ", b[1], wssm, b[2], wssm, b[3])
    print(wsbig)
    print(line)
    print(wsbig)
    print("    ", b[4], wssm, b[5], wssm, b[6])
    print(wsbig)
    print(line)
    print(wsbig)
    print("    ", b[7], wssm, b[8], wssm, b[9])
    print(wsbig)
    print("")

    # time.sleep(2)

def get_human_move(game):
    # Everything to get, record, and display the next human move
    # Turns 1 and 9 are done a little differently
    # When in smart mode (mode 3), need to appropriately transform board
    # after first 3 turns
    if game.turn == 1:
        printboard(game.numboard)

        move = input("Where do you play first? ")
        while move not in game.moves:
            move = input("Where do you play first? Enter the number for the location: ")
        move = int(move)
        game.record[1] = move

        if game.mode == 3:
            # if in smartmode, need to rotate board to get tboard
            # before updating move (including creating key)
            if move == 3 or move == 6:
                game.rotate = 3
            if move == 9 or move == 8:
                game.rotate = 2
            if move == 7 or move == 4:
                game.rotate = 1

    elif game.turn == 9:
        move9 = max(game.moves)
        game.record[9] = int(move9)
        print("There is only one place left to play")
        next = input("Press 'Enter' to see your last move")

    else:
        if game.turn%2 == 1:
            symbol = "X"
        else:
            symbol = "O"

        next = input("Press 'Enter' to pick your next move")
        printboard(game.numboard)
        print("You are playing", symbol)
        move = " "

        while move not in game.moves:
            move = input("Enter your next move location: ")

        move = int(move)
        game.record[game.turn] = move

        if game.turn == 2 and game.mode == 3:
            # rotate board based on move choice
            if move == 3 or move == 6:
                game.rotate = 3
            if move == 9 or move == 8:
                game.rotate = 2
            if move == 7 or move == 4:
                game.rotate = 1

        if game.turn == 3 and game.mode == 3:
            # need to add appropriate board transformation
            # for turn 3 when in smart mode

            if game.record[2] == 1:
            # if AI played in corner turn 2, see if need to flip board along x = -y axis
            # (same as rotate cw by 90, then flip along vertical, first two moves on tboard
            # stay in the same place)
                if move in [2, 3, 6]:
                    game.rotate = 1
                    game.flip = True
            else: # game.trecord = 5
                if game.trecord[1] == 1:
                    # if turn 1 is at 1 on tboard, transformation same as just above, 
                    # but have to add to any rotation that already might be there
                    if game.transform(move) in [2, 3, 6]:
                        game.rotate = (game.rotate + 1) % 4
                        game.flip = True

                else:
                    # turn 1 is at position 2 on tboard; flip if turn 3 on right side
                    if game.transform(move) in [3, 6, 9]:
                        game.flip = True

    game.updateboards(0)
    printboard(game.cleanboard)


def play_random_move(game):
    if game.turn != 1:
        next = input("Press 'Enter' to have the computer play")
        print("")
    print("Computer plays: ")

    AImove = int(game.moves.pop())
    game.record[game.turn] = AImove
    game.updateboards(0)
    printboard(game.cleanboard)




