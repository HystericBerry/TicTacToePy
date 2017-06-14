from Piece import Piece
from GameBoard import GameBoard

class TTTBoard(GameBoard):
    # should remain constant
    width = 3
    height = 3
    
    def __init__(self):
        # always start Tic Tac Toe with player 1 (X)
        super(TTTBoard, self).__init__(-1, TTTBoard.width, TTTBoard.height)
        self.WINNER = 0
        
    def inBounds(self, piece):
        inColRange = 0 <= piece.x and piece.x < self.width
        inRowRange = 0 <= piece.y and piece.y < self.height
        return inColRange and inRowRange

    # Technically, player is defined by turn this means that
    # player does not need to be passed into the add method
    def add(self, x, y):
        piece = Piece(self.TURN, x, y)
        if self.inBounds(piece) and self.board[piece.x][piece.y] == 0:
            self.board[piece.x][piece.y] = piece.player
            self.checkWin(piece) # check for win after every piece is added
            self.TURN = -(self.TURN) # switch player turns
            return True
        return False # probably better to throw an exception

    def checkWin(self, piece):
        # for every direction
        for i in range(-1, 1):
            for j in range(-1, 1):
                if i == 0 and j == 0:
                    continue
                numPiece = 0

                count = 1
                # search one direction
                while True:
                    nextPiece = Piece(0, piece.x+(count*i), piece.y+(count*j))
                    if self.inBounds(nextPiece):
                        if self.board[nextPiece.x][nextPiece.y] == piece.player:
                            numPiece += 1
                    else:
                        break
                    count += 1

                count = 1
                # search other direction
                while True:
                    nextPiece = Piece(0, piece.x-(count*i), piece.y-(count*j))
                    if self.inBounds(nextPiece):
                        if self.board[nextPiece.x][nextPiece.y] == piece.player:
                            numPiece += 1
                    else:
                        break
                    count += 1
                
                if numPiece == 2:
                    self.WINNER = piece.player
                    break

    # Print the Current State of the Board to Console
    def printBoard(self):
        for r in range(self.height):
            row = "["
            for c in range(self.width):
                if c != 0:
                    row += " | "
                if self.board[c][r] == 0:
                    row += " - "
                if self.board[c][r] == -1:
                    row += " X "
                if self.board[c][r] == 1:
                    row += " O "
            row += " ] "
            print(row)
