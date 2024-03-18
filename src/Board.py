import numpy as np


class Board:
    def __init__(self, maxRows=6, maxCols=7):
        self.maxRows = maxRows
        self.maxCols = maxCols
        self.layout = np.zeros((maxRows, maxCols))
        self.gameOver = False

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

    def checkWinningMove(self):
        pieces = (1, 2)

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
                        return piece

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
                        return piece

        return 0

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
                        return piece

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
                        return piece
