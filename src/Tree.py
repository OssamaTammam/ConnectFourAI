class Node:
    def __init__(self, board, parent=None):
        self.parent = parent
        self.children: list[Node] = []
        self.board = board.copy()

    def getChildren(self):
        return self.children

    def getParent(self):
        return self.parent

    def insertChild(self, child):
        self.children.append(child)

    def print(self):
        self.boardValue.printBoard()


class Tree:
    def __init__(self) -> None:
        self.root = None

    def printTree(self):
        self.printNode(self.root, 0)

    def printNode(self, node, depth):
        if node is None:
            return

        indent = "  " * depth
        print(indent + node.print())  # Print the board state of the current node

        for child in node.getChildren():
            self.printNode(child, depth + 1)
