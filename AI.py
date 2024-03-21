import math
from GameState import GameState


class AI:
    @staticmethod
    def minimax(gameState, depth, player, expanded):
        expanded[0] += 1
        if depth == 0 or (
            len(gameState[0]) == 6
            and len(gameState[1]) == 6
            and len(gameState[2]) == 6
            and len(gameState[3]) == 6
            and len(gameState[4]) == 6
            and len(gameState[5]) == 6
            and len(gameState[6]) == 6
        ):
            return gameState, GameState.getHeuristic(gameState)

        neighbors = GameState.calcNeighbors(gameState, player)
        if player == 0:
            bound = -math.inf
            for i in range(len(neighbors)):
                child, value = AI.minimax(neighbors[i], depth - 1, 1, expanded)

                if value > bound:
                    bound = value
                    best = neighbors[i]

            return best, bound

        elif player == 1:
            bound = math.inf
            for i in range(len(neighbors)):
                child, value = AI.minimax(neighbors[i], depth - 1, 0, expanded)

                if value < bound:
                    bound = value
                    best = neighbors[i]

            return best, bound

    @staticmethod
    def minimaxPruning(gameState, depth, player, expanded):
        return AI._minimaxPruning(
            gameState, depth, player, -math.inf, math.inf, expanded
        )

    @staticmethod
    def _minimaxPruning(gameState, depth, player, alpha, beta, expanded):
        expanded[0] += 1
        if depth == 0 or (
            len(gameState[0]) == 6
            and len(gameState[1]) == 6
            and len(gameState[2]) == 6
            and len(gameState[3]) == 6
            and len(gameState[4]) == 6
            and len(gameState[5]) == 6
            and len(gameState[6]) == 6
        ):
            return gameState, GameState.getHeuristic(gameState)

        neighbors = GameState.calcNeighbors(gameState, player)
        if player == 0:
            bound = -math.inf
            for i in range(len(neighbors)):
                child, value = AI._minimaxPruning(
                    neighbors[i], depth - 1, 1, alpha, beta, expanded
                )
                if value > bound:
                    bound = value
                    best = neighbors[i]
                    alpha = max(alpha, value)
                    if beta <= alpha:
                        break
            return best, bound

        elif player == 1:
            bound = math.inf
            for i in range(len(neighbors)):
                child, value = AI._minimaxPruning(
                    neighbors[i], depth - 1, 0, alpha, beta, expanded
                )
                if value < bound:
                    bound = value
                    best = neighbors[i]
                    beta = min(beta, value)
                    if beta <= alpha:
                        break
            return best, bound
