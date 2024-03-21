from collections import deque
from copy import deepcopy
import math
from GameState import GameState


class Tree:
    def __init__(tree, gameState, value, neighbors, player, depth):
        tree.gameState = gameState
        tree.value = value
        tree.neighbors = neighbors
        tree.player = player
        tree.depth = depth

    @staticmethod
    def calcNeighbors(gameState, player):
        neighbors = deque()

        for i in range(7):
            if len(gameState[i]) == 6:
                continue
            gameState[i].append(player)
            neighbors.append(Tree(deepcopy(gameState), None, None, None, None))
            gameState[i].pop()

        return neighbors

    @staticmethod
    def minmax(tree, depth, player, expanded):
        expanded[0] += 1
        # tree.player = player
        # tree.depth = depth

        if depth == 0 or (
            len(tree.gameState[0]) == 6
            and len(tree.gameState[1]) == 6
            and len(tree.gameState[2]) == 6
            and len(tree.gameState[3]) == 6
            and len(tree.gameState[4]) == 6
            and len(tree.gameState[5]) == 6
            and len(tree.gameState[6]) == 6
        ):
            tree.value = GameState.getHeuristic(tree.gameState)
            return tree.gameState, tree.value

        tree.neighbors = Tree.calcNeighbors(tree.gameState, player)
        if player == 0:
            bound = -math.inf

            for i in range(len(tree.neighbors)):
                child, value = Tree.minmax(tree.neighbors[i], depth - 1, 1, expanded)
                if value > bound:
                    bound = value
                    best = tree.neighbors[i]

            tree.value = bound
            return best, bound
        elif player == 1:
            bound = math.inf
            for i in range(len(tree.neighbors)):
                child, value = Tree.minmax(tree.neighbors[i], depth - 1, 0, expanded)
                if value < bound:
                    bound = value
                    best = tree.neighbors[i]

            tree.value = bound
            return best, bound

    @staticmethod
    def _minmaxPruning(tree, depth, player, alpha, beta, expanded):
        expanded[0] += 1
        # tree.player = player
        # tree.depth = depth

        if depth == 0 or (
            len(tree.gameState[0]) == 6
            and len(tree.gameState[1]) == 6
            and len(tree.gameState[2]) == 6
            and len(tree.gameState[3]) == 6
            and len(tree.gameState[4]) == 6
            and len(tree.gameState[5]) == 6
            and len(tree.gameState[6]) == 6
        ):
            tree.value = GameState.getHeuristic(tree.gameState)
            return tree.gameState, tree.value

        tree.neighbors = Tree.calcNeighbors(tree.gameState, player)
        if player == 0:
            bound = -math.inf
            for i in range(len(tree.neighbors)):
                child, value = Tree._minmaxPruning(
                    tree.neighbors[i], depth - 1, 1, alpha, beta, expanded
                )
                if value > bound:
                    bound = value
                    best = tree.neighbors[i]
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break

            tree.value = bound
            return best, bound
        elif player == 1:
            bound = math.inf
            for i in range(len(tree.neighbors)):
                child, value = Tree._minmaxPruning(
                    tree.neighbors[i], depth - 1, 0, alpha, beta, expanded
                )
                if value < bound:
                    bound = value
                    best = tree.neighbors[i]
                    beta = min(beta, value)
                    if beta <= alpha:
                        break

            tree.value = bound
            return best, bound

    def minmaxPruning(tree, depth, player, expanded):
        return Tree._minmaxPruning(tree, depth, player, -math.inf, math.inf, expanded)

    @staticmethod
    def getTree(board):
        boardTree = Tree(board, None, None, None, None)
        return boardTree
