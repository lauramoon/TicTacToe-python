
class Board:
    """
    Defines the game board and all pertinent aspects of the game
    Board positions are 1 - 9, ignoring index 0 in lists
    """

    # sets of winning moves
    winsets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
               {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
               {1, 5, 9}, {3, 5, 7}]

    # Defines the mark (X or O) for the turn. X goes first
    turnmark = {}
    for i in range(1, 11):
        if i % 2 == 0:
            turnmark[i] = "O"
        else:
            turnmark[i] = "X"

    def __init__(self, first, mode):
        # result = -1 if unfinished; 0 is human win; 1 is computer win; 2 is draw
        self.result = -1
        # The printed options
        self.numboard = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # The moves played
        self.cleanboard = [" "]*10
        # Initialize turn number
        self.turn = 1
        # Record of the move played each turn
        self.record = [0]*10
        # Record of the moves played on the transformed board for smart mode
        self.trecord = [0]*10
        # playbook dictionary key to look up next move in smart mode
        self.key = 0
        # who goes first (human - 0; computer - 1)
        self.first = first
        # board rotation for smart mode
        self.rotate = 0
        # whether transformed board is flipped on vertical axis for smart mode
        self.flip = False 
        # valid move options
        self.moves = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
        # moves taken by first player (X) - set of integers
        self.movesX = set()
        # moves taken by second player (O) - set of integers
        self.movesO = set()
        # human-selected game mode (1 - random; 2 - casual; 3 - smart)
        self.mode = mode

    def flipboard(self, position):
        # calculations new position if board flipped on vertical axis
        if self.flip:
            matrix = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]
            fposition = matrix[position]
        else:
            fposition = position

        return fposition

    def rotateboard(self, position, direction):
        # calculates new position if board rotated
        if direction == "cw":
            rotation = self.rotate
        elif direction == "ccw":
            rotation = 4 - self.rotate
        else:
            print("typo in rotation direction")
        print(self.rotate)

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

    def update_board(self, move):
        """
        takes the latest move and adds it to the numbered and clean boards,
        drops the move from possible moves, updates the key (for smart mode),
        updates set of moves and increments turn number
        param move: the move for the current turn
        return: nothing
        """
        # board symbol is X for odd turns, O for even
        symbol = self.turnmark[self.turn]

        # update game record
        self.record[self.turn] = move

        # update numbered and clean boards
        self.numboard[move] = symbol
        self.cleanboard[move] = symbol

        # update moves taken
        if symbol == "X":
            self.movesX.add(move)
        else:
            self.movesO.add(move)

        # update the key
        self.key = self.key*10 + self.trecord[self.turn]

        # drop the last move from the set of possible moves
        self.moves.discard(str(move))

        # increment turn number
        self.turn += 1

    def current_moveset(self):
        """
        returns set of all moves of current player
        return: set of moves of current player
        """
        if self.turnmark[self.turn] == "X":
            moveset = self.movesX
        else:
            moveset = self.movesO

        return moveset

    def previous_moveset(self):
        """
        returns set of all moves of previous player
        return: set of moves of previous player
        """
        if self.turnmark[self.turn] == "X":
            moveset = self.movesO
        else:
            moveset = self.movesX

        return moveset

    def check_for_win(self):
        """
        check if anyone won, used in random and casual mode
        called after boards are updated, so check previous play
        return: True if previous player won, False if no win
        """
        # get the moves of the previous player
        moveset = self.previous_moveset()
        # True if previous player won
        won = False

        # check if each winning set of moves is a subset of last player's moves
        for n in self.winsets:
            if n.issubset(moveset):
                won = True

        return won

    def find_block(self):
        """
        for casual mode, sees if there's a potential win to block
        (could be used to replace later moves in smart move, haven't tried it)
        return: first blocking move found; 0 if none found
        """
        # get the moves of the previous player
        moveset = self.previous_moveset()

        # blocking move. 0 is none
        block = 0

        for n in self.winsets:
            # go through sets of winning moves, see if
            # 1) winning set has two in common with opponent's moves
            # do this by subtracting moveset from winset; true if set has one member
            # 2) see if that member is in available moves. if so, need to play it
            diff = n - moveset
            if len(diff) == 1:
                # get the one move in diff
                move = max(diff)
                # see if it is in the remaining available moves
                if str(move) in self.moves:
                    block = move
                    break
        return block

    def find_winner(self):
        """
        Sees if there's a place to play and win, used for casual mode
        same as find block, but with current player's moves
        return: winning move, or zero if none
        """
        # get current set of moves
        moveset = self.current_moveset()
        # no winning move if 0
        winner = 0

        for n in self.winsets:
            diff = n - moveset
            if len(diff) == 1:
                move = max(diff)
                if str(move) in self.moves:
                    winner = move
                    break
        return winner












