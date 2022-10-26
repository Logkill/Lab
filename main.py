import sys

from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPixmap, QBrush, QPalette


class Labirint(QMainWindow):
    def __init__(self):
        super().__init__()

        self.palette = None
        self.board = None
        self.initUI()

    def initUI(self):
        self.board = Board(self)
        self.setCentralWidget(self.board)
        self.board.start()

        self.resize(500, 500)
        self.setWindowTitle('Лабиринт')

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("ёл2.jpg")))
        self.setPalette(self.palette)
        self.show()


class Board(QFrame):
    BoardWidth = 50
    BoardHeight = 50

    def __init__(self, parent):
        super().__init__(parent)

        self.curPiece = None
        self.numLinesRemoved = None
        self.isWaitingAfterLine = None
        self.isStarted = None
        self.isPaused = None
        self.curY = None
        self.board = None
        self.curX = None
        self.initBoard()

    def initBoard(self):

        self.board = []
        self.setFocusPolicy(Qt.StrongFocus)

    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardWidth

    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardHeight

    def start(self):
        self.isStarted = True
        self.newPiece()

    def paintEvent(self, event):
        painter = QPainter(self)
        boardTop = self.contentsRect().bottom() - Board.BoardHeight * self.squareHeight()

        if self.curPiece.shape():

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSquare(painter, self.contentsRect().left() + x * self.squareWidth(),
                                boardTop + (Board.BoardHeight - y - 1) * self.squareHeight())

    def drawSquare(self, painter, x, y):

        color = QColor(0x66CCCC)
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Left:
            self.tryMove(self.curPiece, self.curX - 1, self.curY)

        if key == Qt.Key_Right:
            self.tryMove(self.curPiece, self.curX + 1, self.curY)

        if key == Qt.Key_Down:
            self.tryMove(self.curPiece, self.curX, self.curY - 1)

        if key == Qt.Key_Up:
            self.tryMove(self.curPiece, self.curX, self.curY + 1)

    def tryMove(self, newPiece, newX, newY):

        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)

            if x < 0 or x >= Board.BoardWidth or y < 0 or y >= Board.BoardHeight:

                return False

        self.curX = newX
        self.curY = newY
        self.update()
        return True

    def newPiece(self):

        self.curPiece = Shape()
        self.curPiece.setShape(5)

        self.curX = Board.BoardWidth // 2 - 24
        self.curY = Board.BoardHeight - 1 + self.curPiece.minY()


class Shape(object):
    coordsTable = (
        ((0, 0), (0, 0), (0, 0), (0, 0)),
        ((0, -1), (0, 0), (-1, 0), (-1, 1)),
        ((0, -1), (0, 0), (1, 0), (1, 1)),
        ((0, -1), (0, 0), (0, 1), (0, 2)),
        ((-1, 0), (0, 0), (1, 0), (0, 1)),
        ((0, 0), (1, 0), (0, 1), (1, 1)),

    )

    def __init__(self):

        self.pieceShape = None
        self.coords = [[0, 0] for _ in range(4)]

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):

        table = Shape.coordsTable[shape]

        for i in range(1):
            for j in range(2):
                self.coords[i][j] = table[i][j]

        self.pieceShape = shape

    def x(self, index):
        return self.coords[index][0]

    def y(self, index):
        return self.coords[index][1]

    def setX(self, index, x):
        self.coords[index][0] = x

    def setY(self, index, y):
        self.coords[index][1] = y

    def minX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = min(m, self.coords[i][0])

        return m

    def maxX(self):

        m = self.coords[0][0]
        for i in range(4):
            m = max(m, self.coords[i][0])

        return m

    def minY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = min(m, self.coords[i][1])

        return m

    def maxY(self):

        m = self.coords[0][1]
        for i in range(4):
            m = max(m, self.coords[i][1])

        return m


if __name__ == '__main__':
    app = QApplication([])
    lab = Labirint()
    sys.exit(app.exec_())
