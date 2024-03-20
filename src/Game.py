import sys
import pygame
import math
from GUI import GUI
from Board import Board
from AI import AI


class Game:
    def __init__(self):
        pygame.init()
        self.board = Board()
        self.gui = GUI(self.board)
        self.turn = 0

    # main game loop
    def refresh(self):
        while not self.board.isGameOver():
            self.gui.drawBoard()
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    sys.exit()

                if self.turn == 0:
                    if event.type == pygame.MOUSEMOTION:
                        self.gui.mouseMotion(event, self.turn)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pygame.draw.rect(
                            self.gui.screen,
                            GUI.BLACK,
                            (0, 0, self.gui.width, self.gui.squareSize),
                        )

                        if self.turn == 0:
                            posx = event.pos[0]
                            col = int(math.floor(posx / self.gui.squareSize))

                            self.board.dropPiece(col, 1)

                            self.board.calculateScores()

                        self.turn += 1
                        self.turn = self.turn % 2
                        self.board.printBoard()

                elif self.turn == 1:
                    col, minMaxScore = AI.minMaxPruning(
                        self.board, 5, -math.inf, math.inf, True
                    )

                    self.board.dropPiece(col, 2)

                    self.board.calculateScores()

                    self.turn += 1
                    self.turn = self.turn % 2
                    self.board.printBoard()

                if self.board.isBoardFull():
                    winner = self.board.calcWinner()
                    self.gui.drawBoard()
                    self.gui.renderWinningScreen(winner)
                    print(self.board.oneScore)
                    print(self.board.twoScore)
                    self.board.gameOver = True
                    pygame.time.wait(3000)
