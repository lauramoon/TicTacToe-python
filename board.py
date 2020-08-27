
class Board:
    """
    Defines the game board and all pertinent aspects of the game
    Board positions are 1 - 9, ignoring index 0 in lists
    """
    # sets of winning moves
    win_sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9},
                {1, 4, 7}, {2, 5, 8}, {3, 6, 9},
                {1, 5, 9}, {3, 5, 7}]

    # Defines the mark (X or O) for the turn. X goes first
    turn_mark = {}
    for i in range(1, 11):
        turn_mark[i] = "O" if i % 2 == 0 else "X"

    def __init__(self, first, mode):
        # result = -1 if unfinished; 0 is human win; 1 is computer win; 2 is draw
        self.result = -1
        # The printed options
        self.num_board = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        # The moves played
        self.clean_board = [" "] * 10
        # Initialize turn number
        self.turn = 1
        # Record of the move played each turn
        self.record = [0]*10
        # Record of the moves played on the transformed board for smart mode
        self.t_record = [0] * 10
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
        """
        for board transformation for smart mode
        calculates new position if board flipped on vertical axis
        :param position: location on regular board
        :return: location on flipped board
        """
        if self.flip:
            matrix = [0, 3, 2, 1, 6, 5, 4, 9, 8, 7]
            f_position = matrix[position]
        else:
            f_position = position

        return f_position

    def rotate_board(self, position, direction):
        """
        calculates new position when board is rotated.
        self.rotate is the clockwise rotation from regular board
        to transformed board. If direction is CCW, have to go opposite
        :param position: location given
        :param direction: cw or ccw
        :return: position when board rotated
        """
        # rotation depends on direction requested
        rotation = self.rotate if direction == "cw" else 4 - self.rotate

        # get new position depending on rotation
        if rotation == 1:
            matrix = [0, 3, 6, 9, 2, 5, 8, 1, 4, 7]
            r_position = matrix[position]
        elif rotation == 2:
            matrix = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
            r_position = matrix[position]
        elif rotation == 3:
            matrix = [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
            r_position = matrix[position]
        else:
            r_position = position

        return r_position

    def transform(self, position):
        """
        used for smart mode when looking up moves
        transforms position from regular board to transformed board
        :param position: location on regular board
        :return: location on transformed board
        """
        r_position = self.rotate_board(position, "cw")
        t_position = self.flipboard(r_position)

        return t_position

    def rev_transform(self, t_position):
        """
        used for smart mode where looking up moves
        takes position on transformed board and gets it for regular board
        :param t_position: location on transformed board
        :return:
        """
        # does the opposite of transform()
        f_position = self.flipboard(t_position)
        position = self.rotate_board(f_position, "ccw")

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
        symbol = self.turn_mark[self.turn]

        # update game record
        self.record[self.turn] = move

        # update numbered and clean boards
        self.num_board[move] = symbol
        self.clean_board[move] = symbol

        # update moves taken
        if symbol == "X":
            self.movesX.add(move)
        else:
            self.movesO.add(move)

        # update the key (used for smart mode)
        self.key = self.key*10 + self.t_record[self.turn]

        # drop the last move from the set of possible moves
        self.moves.discard(str(move))

        # increment turn number
        self.turn += 1

    def check_for_win(self):
        """
        check if anyone won, used in random and casual mode
        called after boards are updated, so check previous play
        return: True if previous player won, False if no win
        """
        # get the moves of the previous player
        move_set = self.movesO if self.turn_mark[self.turn] == "X" else self.movesX
        # True if previous player won
        won = False

        # check if each winning set of moves is a subset of last player's moves
        for n in self.win_sets:
            if n.issubset(move_set):
                won = True
                break

        return won

    def find_block(self):
        """
        for casual mode, sees if there's a potential win to block
        (could be used to replace later moves in smart move, haven't tried it)
        return: first blocking move found; 0 if none found
        """
        # get the moves of the previous player
        move_set = self.movesO if self.turn_mark[self.turn] == "X" else self.movesX

        # blocking move. 0 is none
        block = 0

        for n in self.win_sets:
            # go through sets of winning moves, see if
            # 1) winning set has two in common with opponent's moves
            # do this by subtracting move_set from win_set; true if set has one member
            # 2) see if that member is in available moves. if so, need to play it
            diff = n - move_set
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
        Sees if there's a place to play and win, used for casual mode.
        Same as find block, but with current player's moves
        return: winning move, or zero if none
        """
        # get current set of moves
        move_set = self.movesX if self.turn_mark[self.turn] == "X" else self.movesO
        # no winning move if 0
        winner = 0

        for n in self.win_sets:
            # remove current moves from win_set
            diff = n - move_set
            # if there's one move left, get it
            if len(diff) == 1:
                move = max(diff)
                # and see if it's available to play
                if str(move) in self.moves:
                    winner = move
                    break
        return winner
