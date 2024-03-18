import pygame


class GUI:
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)

    def __init__(self, board, squareSize=100):
        self.board = board
        self.width = board.maxCols * self.squareSize
        self.height = (self.maxRows + 1) * self.squareSize
        self.size = (self.width, self.height)
        self.radius = int(self.squareSize / 2 - 5)
        self.self.screen = pygame.display.set_mode(self.size)

    def drawBoard(self):
        for col in range(self.board.maxCols):
            for row in range(self.board.maxRows):
                pygame.draw.rect(
                    self.self.screen,
                    GUI.BLUE,
                    (
                        col * self.self.squareSize,
                        row * self.self.squareSize + self.self.squareSize,
                        self.self.squareSize,
                        self.self.squareSize,
                    ),
                )
                pygame.draw.circle(
                    self.self.screen,
                    self.BLACK,
                    (
                        int(col * self.self.squareSize + self.self.squareSize / 2),
                        int(
                            row * self.self.squareSize
                            + self.self.squareSize
                            + self.self.squareSize / 2
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

    # TODO: render the screen
    def render(self):
        pass
