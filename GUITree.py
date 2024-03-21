import PySimpleGUI as sg


class GUITree:
    @staticmethod
    def showTree(boardTree):
        layout = [
            [
                sg.Graph(
                    canvas_size=(700, 300),
                    graph_bottom_left=(0, 300),
                    graph_top_right=(700, 0),  # Define the graph area
                    change_submits=True,
                    key="graph",
                    pad=0,
                )
            ]
        ]

        window = sg.Window("Tree", layout, finalize=True)
        graph = window["graph"]
        GUITree.drawTree(graph, boardTree)
        i0 = 0
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break
            if (
                event == "graph"
            ):  # if there's a "Graph" event, then it's a mouse movement. Move the square
                x, y = values["graph"]  # get mouse position
                id = graph.get_figures_at_location(
                    (x, y)
                )  # this function returns the id of the figure clicked
                if len(id) > 0:
                    i = int((id[0] - i0 - 4) / 3)
                    if (
                        0 <= i < len(boardTree.neighbors)
                        and boardTree.neighbors[i].neighbors
                    ):
                        boardTree = boardTree.neighbors[i]
                        i0 = GUITree.drawTree(graph, boardTree)
        window.close()

    @staticmethod
    def drawTree(graph, boardTree):
        graph.erase()
        if not boardTree.player:
            i0 = graph.draw_polygon([(350, 20), (310, 100), (390, 100)], "green")
            graph.draw_text(str(boardTree.value), (350, 70))
            for i in range(len(boardTree.neighbors)):
                graph.draw_line((350, 100), (100 * i + 50, 200))
                graph.draw_polygon(
                    [(100 * i + 10, 200), (100 * i + 90, 200), (100 * i + 50, 280)],
                    "red",
                )
                if boardTree.neighbors[i].value is not None:
                    graph.draw_text(
                        str(boardTree.neighbors[i].value), (100 * i + 50, 230)
                    )
                else:
                    graph.draw_text("x", (100 * i + 50, 230))

        else:
            i0 = graph.draw_polygon([(350, 100), (310, 20), (390, 20)], "red")
            graph.draw_text(str(boardTree.value), (350, 50))
            for i in range(len(boardTree.neighbors)):
                graph.draw_line((350, 100), (100 * i + 50, 200))
                graph.draw_polygon(
                    [(100 * i + 10, 280), (100 * i + 90, 280), (100 * i + 50, 200)],
                    "green",
                )
                if boardTree.neighbors[i].value is not None:
                    graph.draw_text(
                        str(boardTree.neighbors[i].value), (100 * i + 50, 250)
                    )
                else:
                    graph.draw_text("x", (100 * i + 50, 250))
        return i0
