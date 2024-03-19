class AI:
    def __init__(self, board):
        self.board = board

    def getValidMoves(self):
        validLocations = []

        for col in range(self.board.maxCols):
            if self.board.isValidLocation(col):
                validLocations.append(col)

        return validLocations

    def minMax(depth, alpha, beta, maximizingPlayer):
        pass
