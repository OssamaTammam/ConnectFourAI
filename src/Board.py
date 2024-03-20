import numpy as np


class Board:
    def __init__(self, maxRows=6, maxCols=7):
        self.maxRows = maxRows
        self.maxCols = maxCols
        self.layout = np.zeros((maxRows, maxCols))
        self.gameOver = False
        self.oneScore = 0
        self.twoScore = 0
        self.scoredSequences = set()

    def __hash__(self) -> int:
        return self.layout.tobytes()

    def __eq__(self, __value: object) -> bool:
        return np.all(self.board == __value.board)

    def __getitem__(self, indices):
        row, col = indices
        return self.board[row][col]

    def dropPiece(self, col, piece) -> None:
        if self.isValidLocation(col):
            self.layout[self.getNextOpenRow(col)][col] = piece

    def getNextOpenRow(self, col) -> int:
        for row in range(self.maxRows):
            if self.layout[row][col] == 0:
                return row

    def isValidLocation(self, col):
        return self.layout[self.maxRows - 1][col] == 0

    def getBoard(self) -> np.array:
        return self.layout

    def isGameOver(self) -> bool:
        return self.gameOver

    def printBoard(self):
        print(np.flip(self.layout, 0))

    def calculateScores(self):
        pieces = (1, 2)
        sequences = set()

        # check for horizontal win
        for col in range(self.maxCols - 3):
            for row in range(self.maxRows):
                for piece in pieces:
                    if (
                        self.layout[row][col] == piece
                        and self.layout[row][col + 1] == piece
                        and self.layout[row][col + 2] == piece
                        and self.layout[row][col + 3] == piece
                    ):
                        # store that sequence
                        sequence = tuple((row, col + i) for i in range(4))
                        sequences.add(sequence)
                        if sequence not in self.scoredSequences:
                            if piece == 1:
                                self.oneScore += 1
                            else:
                                self.twoScore += 1

        # check for vertical win
        for col in range(self.maxCols):
            for row in range(self.maxRows - 3):
                for piece in pieces:
                    if (
                        self.layout[row][col] == piece
                        and self.layout[row + 1][col] == piece
                        and self.layout[row + 2][col] == piece
                        and self.layout[row + 3][col] == piece
                    ):
                        # store that sequence
                        sequence = tuple((row + i, col) for i in range(4))
                        sequences.add(sequence)
                        if sequence not in self.scoredSequences:
                            if piece == 1:
                                self.oneScore += 1
                            else:
                                self.twoScore += 1

        # check for positive slope win
        for col in range(self.maxCols - 3):
            for row in range(self.maxRows - 3):
                for piece in pieces:
                    if (
                        self.layout[row][col] == piece
                        and self.layout[row + 1][col + 1] == piece
                        and self.layout[row + 2][col + 2] == piece
                        and self.layout[row + 3][col + 3] == piece
                    ):
                        # store that sequence
                        sequence = tuple((row + i, col + i) for i in range(4))
                        sequences.add(sequence)
                        if sequence not in self.scoredSequences:
                            if piece == 1:
                                self.oneScore += 1
                            else:
                                self.twoScore += 1

        # check for negative slope win
        for col in range(self.maxCols - 3):
            for row in range(3, self.maxRows):
                for piece in pieces:
                    if (
                        self.layout[row][col] == piece
                        and self.layout[row - 1][col + 1] == piece
                        and self.layout[row - 2][col + 2] == piece
                        and self.layout[row - 3][col + 3] == piece
                    ):
                        # store that sequence
                        sequence = tuple((row - i, col + i) for i in range(4))
                        sequences.add(sequence)
                        if sequence not in self.scoredSequences:
                            if piece == 1:
                                self.oneScore += 1
                            else:
                                self.twoScore += 1

        self.scoredSequences.update(sequences)

    def calcWinner(self):
        if self.oneScore == self.twoScore:
            return 3
        elif self.oneScore > self.twoScore:
            return 1
        else:
            return 2

    def isBoardFull(self):
        return ~np.any(self.layout == 0)
