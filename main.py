import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication, QMessageBox


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

        self.resize(380, 380)
        self.setWindowTitle('Лабиринт')
        self.show()

        start = QMessageBox()
        start.setWindowTitle('Начало игры')
        start.setText('Начать играть')
        start.setStandardButtons(QMessageBox.Ok)
        start.exec_()


def Game_Over(btn):
    if btn.text() == 'Close':
        sys.exit(app.exec_())


class Board(QFrame):
    BoardW = 21
    BoardH = 21

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

        self.setFocusPolicy(Qt.StrongFocus)

    def squareWidth(self):
        return self.contentsRect().width() // Board.BoardW

    def squareHeight(self):
        return self.contentsRect().height() // Board.BoardH

    def start(self):
        self.isStarted = True
        self.newPiece()

    def paintEvent(self, event):

        painter = QPainter(self)
        boardTop = self.contentsRect().bottom() - Board.BoardH * self.squareHeight()

        self.drawSquare(painter, 12 * self.squareWidth(), boardTop + (Board.BoardH - 7)
                        * self.squareHeight())
        self.drawSquare(painter, 2 * self.squareWidth(), boardTop + (Board.BoardH - 13)
                        * self.squareHeight())
        self.drawSquare(painter, 15 * self.squareWidth(), boardTop + (Board.BoardH - 6)
                        * self.squareHeight())
        self.drawSquare(painter, 18 * self.squareWidth(), boardTop + (Board.BoardH - 8)
                        * self.squareHeight())
        self.drawSquare(painter, 5 * self.squareWidth(), boardTop + (Board.BoardH - 18)
                        * self.squareHeight())
        self.drawSquare(painter, 11 * self.squareWidth(), boardTop + (Board.BoardH - 10)
                        * self.squareHeight())
        self.drawSquare(painter, 6 * self.squareWidth(), boardTop + (Board.BoardH - 7)
                        * self.squareHeight())
        self.drawSquare(painter, 10 * self.squareWidth(), boardTop + (Board.BoardH - 19)
                        * self.squareHeight())
        self.drawSquare(painter, 13 * self.squareWidth(), boardTop + (Board.BoardH - 19)
                        * self.squareHeight())
        self.drawSquare(painter, 13 * self.squareWidth(), boardTop + (Board.BoardH - 20)
                        * self.squareHeight())
        self.drawSquare(painter, 17 * self.squareWidth(), boardTop + (Board.BoardH - 17)
                        * self.squareHeight())
        self.drawSquare(painter, 18 * self.squareWidth(), boardTop + (Board.BoardH - 14)
                        * self.squareHeight())
        for i in range(19):
            self.drawSquare(painter, i * self.squareWidth(), boardTop + (Board.BoardH - 1) * self.squareHeight())
        for i in range(21):
            self.drawSquare(painter, 20 * self.squareWidth(), boardTop + (Board.BoardH - i) * self.squareHeight())
        for i in range(21):
            self.drawSquare(painter, 0 * self.squareWidth(), boardTop + (Board.BoardH - (i + 1))
                            * self.squareHeight())
        for i in range(21):
            self.drawSquare(painter, (i + 2) * self.squareWidth(), boardTop + (Board.BoardH - 21)
                            * self.squareHeight())
        for i in range(10):
            self.drawSquare(painter, (i + 2) * self.squareWidth(), boardTop + (Board.BoardH - 3)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, (i + 13) * self.squareWidth(), boardTop + (Board.BoardH - 3)
                            * self.squareHeight())
        for i in range(5):
            self.drawSquare(painter, 11 * self.squareWidth(), boardTop + (Board.BoardH - (i + 3))
                            * self.squareHeight())
        for i in range(5):
            self.drawSquare(painter, 13 * self.squareWidth(), boardTop + (Board.BoardH - (i + 3))
                            * self.squareHeight())
        for i in range(9):
            self.drawSquare(painter, 2 * self.squareWidth(), boardTop + (Board.BoardH - (i + 3))
                            * self.squareHeight())
        for i in range(3):
            self.drawSquare(painter, 3 * self.squareWidth(), boardTop + (Board.BoardH - (i + 11))
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, 18 * self.squareWidth(), boardTop + (Board.BoardH - (i + 2))
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 15) * self.squareWidth(), boardTop + (Board.BoardH - 5)
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 15) * self.squareWidth(), boardTop + (Board.BoardH - 7)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, (i + 13) * self.squareWidth(), boardTop + (Board.BoardH - 9)
                            * self.squareHeight())
        for i in range(9):
            self.drawSquare(painter, (i + 11) * self.squareWidth(), boardTop + (Board.BoardH - 11)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, i * self.squareWidth(), boardTop + (Board.BoardH - 19)
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 2) * self.squareWidth(), boardTop + (Board.BoardH - 17)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, (i + 2) * self.squareWidth(), boardTop + (Board.BoardH - 15)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, 7 * self.squareWidth(), boardTop + (Board.BoardH + (i - 20))
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, (i + 4) * self.squareWidth(), boardTop + (Board.BoardH - 5)
                            * self.squareHeight())
        for i in range(5):
            self.drawSquare(painter, 4 * self.squareWidth(), boardTop + (Board.BoardH - (i + 5))
                            * self.squareHeight())
        for i in range(5):
            self.drawSquare(painter, 9 * self.squareWidth(), boardTop + (Board.BoardH - (i + 5))
                            * self.squareHeight())
        for i in range(3):
            self.drawSquare(painter, (i + 9) * self.squareWidth(), boardTop + (Board.BoardH - 9)
                            * self.squareHeight())
        for i in range(5):
            self.drawSquare(painter, 5 * self.squareWidth(), boardTop + (Board.BoardH - (i + 9))
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 6) * self.squareWidth(), boardTop + (Board.BoardH - 13)
                            * self.squareHeight())
        for i in range(7):
            self.drawSquare(painter, 7 * self.squareWidth(), boardTop + (Board.BoardH - (i + 7))
                            * self.squareHeight())
        for i in range(9):
            self.drawSquare(painter, 9 * self.squareWidth(), boardTop + (Board.BoardH - (i + 11))
                            * self.squareHeight())
        for i in range(7):
            self.drawSquare(painter, 11 * self.squareWidth(), boardTop + (Board.BoardH - (i + 13))
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 12) * self.squareWidth(), boardTop + (Board.BoardH - 17)
                            * self.squareHeight())
        for i in range(3):
            self.drawSquare(painter, 15 * self.squareWidth(), boardTop + (Board.BoardH - (i + 17))
                            * self.squareHeight())
        for i in range(3):
            self.drawSquare(painter, 18 * self.squareWidth(), boardTop + (Board.BoardH - (i + 17))
                            * self.squareHeight())
        for i in range(4):
            self.drawSquare(painter, (i + 15) * self.squareWidth(), boardTop + (Board.BoardH - 19)
                            * self.squareHeight())
        for i in range(8):
            self.drawSquare(painter, (i + 11) * self.squareWidth(), boardTop + (Board.BoardH - 13)
                            * self.squareHeight())
        for i in range(6):
            self.drawSquare(painter, (i + 13) * self.squareWidth(), boardTop + (Board.BoardH - 15)
                            * self.squareHeight())
        if self.curPiece.shape():

            for i in range(4):
                x = self.curX + self.curPiece.x(i)
                y = self.curY - self.curPiece.y(i)
                self.drawSq(painter, self.contentsRect().left() + x * self.squareWidth(),
                            boardTop + (Board.BoardH - y - 1) * self.squareHeight())

    def drawSq(self, painter, x, y):
        color = QColor(0x2d70b7)
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

    def drawSquare(self, painter, x, y):

        color = QColor(0x66CCCC)
        painter.fillRect(x + 1, y + 1, self.squareWidth() - 2,
                         self.squareHeight() - 2, color)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Left:
            self.Move(self.curPiece, self.curX - 1, self.curY)

        if key == Qt.Key_Right:
            self.Move(self.curPiece, self.curX + 1, self.curY)

        if key == Qt.Key_Down:
            self.Move(self.curPiece, self.curX, self.curY - 1)

        if key == Qt.Key_Up:
            self.Move(self.curPiece, self.curX, self.curY + 1)

    def Move(self, newPiece, newX, newY):
        s = []
        f = open('coord.txt')
        for i in f:
            s.append(i)
        b = ("''".join(s))

        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= Board.BoardW or y < 0 or y >= Board.BoardH or str([x, y]) in b:
                return False
        self.curX = newX
        self.curY = newY
        self.update()
        if [newX, newY] == [19, 0]:
            win = QMessageBox()
            win.setText('Вы победили!')
            win.setWindowTitle('Игра окончена!')
            win.setStandardButtons(QMessageBox.Close)
            win.buttonClicked.connect(Game_Over)
            win.exec_()
        return True

    def newPiece(self):

        self.curPiece = Shape()
        self.curPiece.setShape(5)

        self.curX = Board.BoardW // 2 - 9
        self.curY = Board.BoardH - 1 + self.curPiece.minY()


class Shape(object):
    def __init__(self):

        self.pieceShape = None
        self.coords = [[0, 0] for _ in range(4)]

    def shape(self):
        return self.pieceShape

    def setShape(self, shape):

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
