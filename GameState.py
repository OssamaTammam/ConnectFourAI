from collections import deque
import copy


class GameState:
    PLAYER = 1
    AI = 0

    def __init__(self, state):
        board = state
        self.neighbors

    @staticmethod
    def getHeuristic(board):
        return GameState.calcHeuristic(board, GameState.AI) - GameState.calcHeuristic(
            board, GameState.PLAYER
        )

    @staticmethod
    def calcHeuristic(board, player):
        colHeuristic = 0  # column
        for i in range(7):  # column by column
            for j in range(0, 3):  # check every 4 consecutive places
                sum = 0  # number of red bits
                for k in range(j, j + 4):
                    if k >= len(board[i]):
                        continue
                    if board[i][k] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                if sum:
                    colHeuristic += 2**sum

        rowHeuristic = 0  # row
        for j in range(6):
            for i in range(4):
                sum = 0
                for k in range(i, i + 4):
                    if len(board[k]) < j + 1:  # revise
                        continue
                    elif board[k][j] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                if sum:
                    rowHeuristic += 2**sum

        diagonalHeuristic1 = 0  # diagonal1
        for k in range(3):  # diagonal 1 part 2
            j_initial = 5
            i_initial = k + 1
            for counter in range(
                3 - k
            ):  # number of 4 consecutive places in this diagonal
                i = i_initial + counter  # start point
                j = j_initial - counter
                sum = 0
                limit = j - 4
                while j > limit:
                    if len(board[i]) < j + 1:
                        i += 1
                        j -= 1
                        continue
                    elif board[i][j] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                    i += 1
                    j -= 1
                if sum:
                    diagonalHeuristic1 += 2**sum
        for k in range(3):  # diagonal 1 part 1
            j_initial = k + 3
            i_initial = 0
            for counter in range(
                k + 1
            ):  # number of 4 consecutive places in this diagonal
                i = i_initial + counter  # start point
                j = j_initial - counter
                sum = 0
                limit = j - 4
                while j > limit:
                    if len(board[i]) < j + 1:
                        i += 1
                        j -= 1
                        continue
                    elif board[i][j] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                    i += 1
                    j -= 1
                if sum:
                    diagonalHeuristic1 += 2**sum

        diagonalHeuristic2 = 0  # diagonal 2
        for k in range(3):  # diagonal 2 part 1
            j_initial = 3 + k
            i_initial = 6
            for counter in range(
                k + 1
            ):  # num is number of 4 consecutive places in this diagonal
                i = i_initial - counter  # start point
                j = j_initial - counter
                sum = 0
                limit = j - 4
                while j > limit:
                    if len(board[i]) < j + 1:
                        i -= 1
                        j -= 1
                        continue
                    elif board[i][j] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                    i -= 1
                    j -= 1
                if sum:
                    diagonalHeuristic2 += 2**sum
        for k in range(3):  # diagonal 2 part 2
            j_initial = 5
            i_initial = 5 - k
            for counter in range(
                3 - k
            ):  # number of 4 consecutive places in this diagonal
                i = i_initial - counter  # start point
                j = j_initial - counter
                sum = 0
                limit = j - 4
                while j > limit:
                    if len(board[i]) < j + 1:
                        i -= 1
                        j -= 1
                        continue
                    elif board[i][j] == player:
                        sum += 1
                    else:
                        sum = 0
                        break
                    i -= 1
                    j -= 1

        return colHeuristic + rowHeuristic + diagonalHeuristic1 + diagonalHeuristic2

    @staticmethod
    def calcNeighbors(board, player):
        neighbors = deque()
        for i in range(7):
            if len(board[i]) == 6:
                continue

            board[i].append(player)
            neighbors.append(copy.deepcopy(board))
            board[i].pop()

        return neighbors
