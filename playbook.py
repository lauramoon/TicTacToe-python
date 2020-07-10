class Playbook():
    # define dictionary where key n is the integer that looks like
    # the string of moves already taken on transformed board
    # value is list of (1) next move and (2) game result, where
    playbook = {}

    # turn 4 moves (in 3 sets: corner first, side first, center first)
    playbook.update([(154, [7, -1]), (157, [4, -1]), (158, [4, -1]), (159, [2, -1])])
    playbook.update([(251, [3, -1]), (254, [7, -1]), (257, [1, -1]), (258, [3, -1])])
    playbook.update([(514, [6, -1]), (517, [3, -1]), (518, [2, -1]), (519, [3, -1])])

    # turn 5 moves
    playbook.update([(5137, [4, -1]), (5237, [9, -1])])
    for x in [5132, 5134, 5136, 5138, 5139, 5231, 5234, 5236, 5238, 5239]:
        # all the wrong moves for the human
        playbook[x] = [7, 1]

    # turn 6 moves
    # Set 1: human plays in corner first
    playbook[15473] = [2, -1]
    for x in [15462, 15467, 15468, 15469]:
        playbook[x] = [3, 1]
    playbook[15746] = [2, -1]
    for x in [15742, 15743, 15748, 15749]:
        playbook[x] = [6, 1]
    playbook[15846] = [3, -1]
    for x in [15842, 15843, 15847, 15849]:
        playbook[x] = [6, 1]
    playbook[15928] = [7, -1]
    for x in [15923, 15924, 15926, 15927]:
        playbook[x] = [8, 1]

    # Turn 6 Set 2: human plays on side first
    playbook[25137] = [4, -1]
    for x in [25134, 25136, 25138, 25139]:
        playbook[x] = [7, 1]
    playbook[25473] = [1, -1]
    for x in [25471, 25476, 25478, 25479]:
        playbook[x] = [3, 1]
    playbook[25719] = [8, -1]
    for x in [25713, 25714, 25716, 25718]:
        playbook[x] = [9, 1]
    playbook[25837] = [9, -1]
    for x in [25831, 25834, 25836, 25839]:
        playbook[x] = [7, 1]

    # Turn 6 set 3: human plays in center first
    playbook[51462] = [8, -1]
    playbook[51463] = [7, -1]
    playbook[51467] = [3, -1]
    playbook[51468] = [2, -1]
    playbook[51469] = [3, -1]
    playbook[51732] = [8, -1]
    for x in [51734, 51736, 51738, 51739]:
        playbook[x] = [2, 1]
    playbook[51823] = [7, -1]
    for x in [51824, 51826, 51827, 51829]:
        playbook[x] = [3, 1]
    playbook[51932] = [8, -1]
    for x in [51934, 51936, 51937, 51938]:
        playbook[x] = [2, 1]

    # Turn 7
    playbook[513746] = [8, -1]
    for x in [513742, 513748, 512749]:
        playbook[x] = [6, 1]
    playbook[523791] = [6, 1]
    for x in [523794, 523796, 523798]:
        playbook[x] = [1, 1]

    # Turn 8 has so many options...
    # would be more efficient to switch to casual mode
    # for the last few moves, but that hasn't been written yet
    playbook[1547328] = [6, -1]
    playbook[1547326] = [8, 1]
    playbook[1547329] = [8, 1]
    playbook[1574628] = [9, -1]
    playbook[1574623] = [8, 1]
    playbook[1574629] = [8, 1]

    playbook[1584637] = [9, -1]
    playbook[1584632] = [7, 1]
    playbook[1584639] = [7, 1]
    playbook[1592873] = [6, -1]
    playbook[1592874] = [3, 1]
    playbook[1592876] = [3, 1]

    playbook[2513746] = [8, -1]
    playbook[2513748] = [6, 1]
    playbook[2513749] = [6, 1]
    playbook[2547319] = [6, -1]
    playbook[2547316] = [9, 1]
    playbook[2547318] = [9, 1]

    playbook[2571983] = [6, -1]
    playbook[2571986] = [3, -1]
    playbook[2571984] = [3, -1]
    playbook[2583791] = [6, 1]
    playbook[2583794] = [6, 1]
    playbook[2583796] = [1, 1]

    playbook[5146283] = [7, -1]
    playbook[5146287] = [3, -1]
    playbook[5146289] = [3, -1]
    playbook[5146378] = [2, -1]
    playbook[5146372] = [8, -1]
    playbook[5146379] = [2, -1]
    playbook[5146739] = [8, -1]
    playbook[5146732] = [9, 1]
    playbook[5146738] = [9, 1]
    playbook[5146823] = [7, -1]
    playbook[5146827] = [3, 1]
    playbook[5146829] = [3, 1]
    playbook[5146932] = [8, -1]
    playbook[5146938] = [2, 1]
    playbook[5146937] = [2, 1]

    playbook[5173284] = [6, -1]
    playbook[5173286] = [4, -1]
    playbook[5173289] = [6, -1]

    playbook[5182374] = [6, -1]
    playbook[5182376] = [4, 1]
    playbook[5182379] = [4, 1]

    playbook[5193284] = [6, -1]
    playbook[5193286] = [4, -1]
    playbook[5193287] = [4, -1]

    # Turn 9
    playbook[51374682] = [9, 2]
    playbook[51374689] = [2, 1]


    def __init__ (self, key):
        self.key = key

    def getresult(self):
        return self.playbook[self.key]






