from common import printboard
moves = input("Enter move string: ")

b = [" "]*10
number = len(moves)
print(number)

for i in range(0, number):
    move = int(moves[i])

    if i % 2 == 1:
        symb = "X"
    else:
        symb = "O"
    b[move] = symb

printboard(b)
