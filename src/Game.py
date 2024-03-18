import sys
import pygame
import math
from GUI import GUI
from Board import Board


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

                        winner = self.board.checkWinningMove()
                        if winner:
                            self.gui.renderWinningScreen(winner)
                            self.board.gameOver = True
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.gui.squareSize))

                        self.board.dropPiece(col, 2)

                        winner = self.board.checkWinningMove()
                        if winner:
                            self.gui.renderWinningScreen(winner)
                            self.board.gameOver = True

                    self.turn += 1
                    self.turn = self.turn % 2

                    if self.board.isGameOver():
                        pygame.time.wait(3000)
