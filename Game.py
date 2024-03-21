import time
from datetime import datetime
import PySimpleGUI as sg
from bitarray import bitarray
from AI import AI
from GameState import GameState
from Tree import Tree
from GUITree import GUITree


class Game:
    def __init__(self):
        self.algorithms = ["min-max", "alpha-beta"]
        self.guiLayout = [
            [
                sg.Text(
                    "Connect-4",
                    font="Ravie",
                    size=(28, 1),
                    text_color="black",
                    justification="center",
                )
            ],
            [
                sg.Button(key="new game", button_text="New Game", size=(9, 1)),
                sg.Combo(
                    self.algorithms,
                    key="method",
                    default_value=self.algorithms[0],
                    size=(10, 1),
                ),
                sg.Text("K=", text_color="black"),
                sg.Input(size=(5, 1), key="k", default_text="1"),
                sg.Text("Time Taken: \nNodes Expanded: ", text_color="black"),
                sg.Text(key="t"),
                sg.Button("Show Tree", visible=False),
            ],
            [
                sg.Graph(
                    canvas_size=(490, 420),
                    graph_top_right=(490, 0),
                    graph_bottom_left=(0, 420),
                    background_color="#0040ff",
                    enable_events=True,
                    key="graph",
                )
            ],
        ]
        self.window = sg.Window("Connect4", self.guiLayout, finalize=True)
        self.graph = self.window["graph"]
        self.circles = [[0] * 7] * 6
        self.turn = 0
        self.board = []
        self.newGame()

    def newGame(self):
        # init new board
        self.turn = 0
        self.board = []
        for _ in range(7):
            self.board.append(bitarray())

        # clear out gui board
        for row in range(6):
            for col in range(7):
                self.circles[row][col] = self.graph.draw_circle(
                    center_location=(70 * col + 35, 70 * row + 35),
                    radius=30,
                    fill_color="white",
                )

    def gameLoop(self):
        while True:
            event, values = self.window.read()

            if event == "new game":
                self.newGame()

            if event == "graph":
                x, y = values["graph"]
                col = x // 70
                place = len(self.board[col])

                if place < 6:
                    row = 5 - place
                    x = col * 70 + 35
                    y = row * 70 + 35
                    self.board[col].append(True)
                    newCircle = self.graph.draw_circle((x, 0), 30, "red")

                    for i in range(y):
                        time.sleep(0.001)
                        self.graph.MoveFigure(newCircle, 0, 1)
                        self.window.refresh()

                    expanded = [0]

                    if values["method"] == "min-max":
                        start = datetime.now().minute * 60 + datetime.now().second

                        if int(values["k"]) <= 4:
                            boardTree = Tree.getTree(self.board)
                            childTree, h = Tree.minmax(
                                boardTree, int(values["k"]), 0, expanded
                            )
                            self.window["Show Tree"].update(visible=True)
                            child = childTree.gameState
                        else:
                            self.window["Show Tree"].update(visible=False)
                            child, h = AI.minimax(
                                self.board, int(values["k"]), 0, expanded
                            )

                        self.window["t"].update(
                            str(
                                datetime.now().minute * 60
                                + datetime.now().second
                                - start
                            )
                            + "s\n"
                            + str(expanded[0])
                        )

                    elif values["method"] == "alpha-beta":
                        start = datetime.now().minute * 60 + datetime.now().second
                        if int(values["k"]) <= 4:
                            boardTree = Tree.getTree(self.board)
                            childTree, h = Tree.minmaxPruning(
                                boardTree, int(values["k"]), 0, expanded
                            )
                            self.window["Show Tree"].update(visible=True)
                            child = childTree.gameState
                        else:
                            self.window["Show Tree"].update(visible=False)
                            child, h = AI.minimaxPruning(
                                self.board, int(values["k"]), 0, expanded
                            )

                        self.window["t"].update(
                            str(
                                datetime.now().minute * 60
                                + datetime.now().second
                                - start
                            )
                            + "s\n"
                            + str(expanded[0])
                        )

                    for i in range(7):
                        if len(child[i]) - len(self.board[i]):
                            col = i
                            break

                    place = len(self.board[col])
                    row = 5 - place
                    x = col * 70 + 35
                    y = row * 70 + 35
                    self.board[col].append(False)
                    newCircle = self.graph.draw_circle((x, 0), 30, "green")

                    for i in range(y):
                        time.sleep(0.001)
                        self.graph.MoveFigure(newCircle, 0, 1)
                        self.window.refresh()
                    self.turn += 1

                    if self.turn == 21:
                        Computer = int(GameState.calcHeuristic(self.board, 0) / 16)
                        Player = int(GameState.calcHeuristic(self.board, 1) / 16)
                        sg.popup(
                            "Game ended\nComputer score = "
                            + str(Computer)
                            + "\nUser score = "
                            + str(Player)
                        )

            if event == "Show Tree":
                GUITree.showTree(boardTree)

            if event == sg.WIN_CLOSED:
                break


game = Game()
game.gameLoop()
