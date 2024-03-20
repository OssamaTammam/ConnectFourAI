from math import inf
from random import choice
from Tree import Tree, Node


class AI:
    AI_PIECE = 2
    USER_PIECE = 1

    def __init__(self, board):
        self.board = board
        self.minMaxTree = Tree()

    @staticmethod
    def getValidMoves(board):
        validLocations = []

        for col in range(board.maxCols):
            if board.isValidLocation(col):
                validLocations.append(col)

        return validLocations

    @staticmethod
    def isTerminal(board):
        return len(AI.getValidMoves(board)) == 0

    @staticmethod
    def evaluateBoard(board):
        aiScore = board.getTwoScore()
        userScore = board.getOneScore()
        score = aiScore - userScore
        return score

    def minMaxPruning(self, node, depth, alpha, beta, maximizingPlayer):
        if self.minMaxTree.root is None:
            self.minMaxTree.root = node

        validMoves = AI.getValidMoves(node.board)

        if AI.isTerminal(node.board) or depth == 0:
            return None, AI.evaluateBoard(node.board)

        if maximizingPlayer:
            utility = -inf
            column = choice(validMoves)

            for col in validMoves:
                newNode = Node(node.board.copy())

                newNode.board.dropPiece(col, AI.AI_PIECE)
                node.insertChild(newNode)

                newScore = self.minMaxPruning(newNode, depth - 1, alpha, beta, False)[1]

                if newScore > utility:
                    utility = newScore
                    column = col

                alpha = max(alpha, utility)
                if alpha >= beta:
                    break

            return column, utility

        else:
            utility = inf
            column = choice(validMoves)

            for col in validMoves:
                newNode = Node(node.board.copy())

                newNode.board.dropPiece(col, AI.USER_PIECE)
                node.insertChild(newNode)

                newScore = self.minMaxPruning(newNode, depth - 1, alpha, beta, False)[1]

                if newScore < utility:
                    utility = newScore
                    column = col

                beta = min(alpha, utility)
                if alpha >= beta:
                    break

            return column, utility

    @staticmethod
    def minMaxWithoutPruning(self, board, depth, maximizingPlayer):
        validMoves = AI.getValidMoves(board)

        if AI.isTerminal(board) or depth == 0:
            return None, AI.evaluateBoard(board)

        if maximizingPlayer:
            utility = -inf
            column = choice(validMoves)

            for col in validMoves:
                boardCopy = board.copy()

                boardCopy.dropPiece(col, AI.AI_PIECE)
                newScore = self.minMaxWithoutPruning(boardCopy, depth - 1, False)[1]

                if newScore > utility:
                    utility = newScore
                    column = col

            return column, utility

        else:
            utility = inf
            column = choice(validMoves)

            for col in validMoves:
                boardCopy = board.copy()

                boardCopy.dropPiece(col, AI.USER_PIECE)
                newScore = self.minMaxWithoutPruning(boardCopy, depth - 1, True)[1]

                if newScore < utility:
                    utility = newScore
                    column = col

            return column, utility
