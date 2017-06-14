class GameBoard:
    def __init__(self, turn, width, height):
        self.TURN, self.width, self.height = turn, width, height
        self.board = [[0 for x in range(self.width)] for y in range(self.height)]
