
class Board():
    # Defines the game board
    # board positions are 1 - 9; initial 0 in lists is ignored

    # sets of winning moves
    winsets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
               {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
               {1, 5, 9}, {3, 5, 7}]

    def __init__(self, first, mode):
        # result = -1 is unfinished; 0 is human win; 1 is computer win; 2 is draw
        self.result = -1
        self.numboard = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # The printed options
        self.cleanboard = [" "]*10
        # The moves played
        self.tboard = [" "]*10
        # The moves played on the transformed board (unused?)
        self.turn = 1
        # Initialize turn number
        self.record = [0]*10
        # Record of the move played each turn
        self.trecord = [0]*10
        # Record of the moves played on the transformed board
        self.key = 0
        # playbook dictionary key to look up next move in smart mode
        self.first =first
        # who goes first
        self.rotate = 0
        # board rotation
        self.flip = False 
        # whether transformed board is flipped on vertical axis
        self.moves = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        # valid move options for human
        self.mode = mode
        # human-selected game mode (1 - random; 2 - casual; 3 - smart)

    def flipboard(self, position):
        # calculations new position if board flipped on vertical axis
        if self.flip == True:
            matrix = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]
            fposition = matrix[position]
        else:
            fposition = position

        return fposition

    def rotateboard(self, position, direction):
        if direction == "cw":
            rotation = self.rotate
        elif direction == "ccw":
            rotation = 4 - self.rotate
        else:
            print("typo in rotation direction")

        if rotation == 1:
            matrix = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
            rposition = matrix[position]
        elif rotation == 2:
            matrix = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            rposition = matrix[position]
        elif rotation == 3:
            matrix = [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
            rposition = matrix[position]
        else:
            rposition = position

        return rposition

    def transform(self, position):
        # calculates position after rotating and/or flipping board
        # there's got to be a matrix algebra solution...
        rposition = self.rotateboard(position, "cw")
        tposition = self.flipboard(rposition)

        return tposition

    def rev_transform(self, tposition):
        # does the opposite of transform
        fposition = self.flipboard(tposition)
        # print("fposition", fposition)
        position = self.rotateboard(fposition, "ccw")

        return position

    def updateboards(self, p):
        # takes the latest move and adds it to the numbered board,
        # the clean board, and the transformed board; increments turn number
        # p is the player - human (0) plays on board
        # smart AI (1) plays on transformed board
        # random and casual AI (0) just play on board, no tranformations

        # board symbol is X for odd turns, O for even
        if self.turn%2 == 1:
            symbol = "X"
        else:
            symbol = "O"

        if p == 0:
            # get placement of last move
            position = self.record[self.turn]
            tposition = self.transform(position)
            self.trecord[self.turn] = tposition
        else:
            # last move is in the trecord if AI just played
            tposition = self.trecord[self.turn]
            # print("tposition", tposition)
            position = self.rev_transform(tposition)
            # print("position", position)
            self.record[self.turn] = position

        self.numboard[position] = symbol
        self.cleanboard[position] = symbol
        self.tboard[tposition] = symbol

        self.key = self.key*10 + self.trecord[self.turn]
        # the key is an integer that looks like the string of turns already taken
        self.moves.discard(str(position))
        self.turn += 1

    def get_moveset(self, x):
         # set of all moves of (x = 0) previous player or (x = 1) current player
        moveset = set()
        choice = self.turn + x
        if choice % 2 == 0:
            # create set of X's moves
            for n in [1, 3, 5, 7, 9]:
                moveset.add(self.record[n])
        else:
            # create set of O's moves
            for n in [2, 4, 6, 8]:
                moveset.add(self.record[n])

        return moveset

    def check_for_win(self):
        # for random and casual modes, check if anyone won
        # called after boards are updated, so check for previous play
        moveset = self.get_moveset(0)
        won = False # True if previous player won

        # check if each winning set of moves is a subset of last player's moves
        for n in range(0, 8):
            if self.winsets[n].issubset(moveset):
                won = True

        return won

    def find_block(self):
        # for causual mode, sees if there's a potential win to block
        # maybe could be used to replace later moves in smart move, haven't tried
        moveset = self.get_moveset(0) # moves of opponent
        block = 0 #blocking move. 0 is none

        for n in range(0, 8):
            # go through sets of winning moves, see if
            # 1) winning set has two in common with opponemt's moves
            # do this by subtacting moveset from winset; true if set has one member
            # 2) see if that member is in avaiable moves. if so, need to play it
            diff = self.winsets[n] - moveset
            if len(diff) == 1:
                move = max(diff)
                if str(move) in self.moves:
                    block = move
                    break
        return block

    def find_winner(self):
        # sees if there's a place to play and win, used for casual mode
        # same as find block, but with current player's moves
        moveset = self.get_moveset(1)
        winner = 0 # no winning move if 0

        for n in range(0, 8):
            diff = self.winsets[n] - moveset
            if len(diff) == 1:
                move = max(diff)
                if str(move) in self.moves:
                    winner = move
                    break
        return winner












