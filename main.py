from TTTBoard import TTTBoard

board = TTTBoard()

print("\n\n**********INITIAL TIC TAC TOE BOARD**********\n")
board.printBoard()

P1, P2 = -1, 1

userInput = None
while board.WINNER == 0:
    if board.TURN == P1:
        print("\n\nPlayer 1's turn (X).")
    elif board.TURN == P2:
        print("\n\nPlayer 2's turn (O).")

    # Only expects a list of ints
    print("Enter x y separated by spaces: ")
    userInput = input()
    if userInput == "quit":
        break

    move = [int(i) for i in userInput.split()]

    if len(move) == 2:
        print("Move made: ", move)
        x, y = move[0], move[1]
        if board.add(x, y):
            print("Piece<%d, %d> was added." % (x, y))
            board.printBoard()
        else:
            print("Illegal Piece<%d, %d> was NOT added." % (x, y))
    else:
       print("Illegal Move: ", move)

if board.WINNER == P1:
    print("\n\nPlayer 1 wins (X)!")
elif board.WINNER == P2:
    print("\n\nPlayer 2 wins! (O)")
