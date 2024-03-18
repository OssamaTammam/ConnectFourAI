import pygame


class GUI:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, board, squareSize=100):
        self.board = board
        self.squareSize = squareSize
        self.width = board.maxCols * self.squareSize
        self.height = (self.board.maxRows + 1) * self.squareSize
        self.size = (self.width, self.height)
        self.radius = int(self.squareSize / 2 - 5)
        self.screen = pygame.display.set_mode(self.size)
        self.font = pygame.font.SysFont("monospace", 75)

    def drawBoard(self):
        for col in range(self.board.maxCols):
            for row in range(self.board.maxRows):
                pygame.draw.rect(
                    self.screen,
                    GUI.BLUE,
                    (
                        col * self.squareSize,
                        row * self.squareSize + self.squareSize,
                        self.squareSize,
                        self.squareSize,
                    ),
                )
                pygame.draw.circle(
                    self.screen,
                    self.BLACK,
                    (
                        int(col * self.squareSize + self.squareSize / 2),
                        int(
                            row * self.squareSize
                            + self.squareSize
                            + self.squareSize / 2
                        ),
                    ),
                    self.radius,
                )

        for col in range(self.board.maxCols):
            for row in range(self.board.maxRows):
                if self.board.getBoard()[row][col] == 1:
                    pygame.draw.circle(
                        self.screen,
                        GUI.RED,
                        (
                            int(col * self.squareSize + self.squareSize / 2),
                            self.height
                            - int(row * self.squareSize + self.squareSize / 2),
                        ),
                        self.radius,
                    )
                elif self.board.getBoard()[row][col] == 2:
                    pygame.draw.circle(
                        self.screen,
                        GUI.YELLOW,
                        (
                            int(col * self.squareSize + self.squareSize / 2),
                            self.height
                            - int(row * self.squareSize + self.squareSize / 2),
                        ),
                        self.radius,
                    )

        pygame.display.update()

    def mouseMotion(self, event, turn):
        pygame.draw.rect(self.screen, GUI.BLACK, (0, 0, self.width, self.squareSize))
        posx = event.pos[0]
        if turn == 0:
            pygame.draw.circle(
                self.screen, GUI.RED, (posx, int(self.squareSize / 2)), self.radius
            )
        else:
            pygame.draw.circle(
                self.screen, GUI.YELLOW, (posx, int(self.squareSize / 2)), self.radius
            )
        pygame.display.update()

    def renderWinningScreen(self, player):
        pygame.display.update()
        if player == 1:
            label = self.font.render("Player 1 wins!!", 1, GUI.RED)
        else:
            label = self.font.render("Player 2 wins!!", 1, GUI.YELLOW)
        self.screen.blit(label, (40, 10))
        pygame.display.update()
