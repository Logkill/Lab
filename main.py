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

        self.a = [[0, 20], [0, 19], [0, 18], [0, 17], [0, 16], [0, 15], [0, 14], [0, 13], [0, 12], [0, 11], [0, 10],
                  [0, 9], [0, 8], [0, 7], [0, 6], [0, 5], [0, 4], [0, 3], [0, 2], [0, 1], [0, 0], [1, 0], [2, 0],
                  [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0], [12, 0], [13, 0], [14, 0],
                  [15, 0], [16, 0], [17, 0], [18, 0], [20, 0], [20, 1], [20, 2], [20, 3], [20, 4], [20, 5],
                  [20, 6], [20, 7], [20, 8], [20, 9], [20, 10], [20, 11], [20, 12], [20, 13], [20, 14], [20, 15],
                  [20, 16], [20, 17], [20, 18], [20, 19], [20, 20], [19, 20], [18, 20], [17, 20], [16, 20], [15, 20],
                  [14, 20], [13, 20], [12, 20], [11, 20], [10, 20], [9, 20], [8, 20], [7, 20], [6, 20], [5, 20],
                  [4, 20], [3, 20], [2, 20], [1, 18], [2, 18], [3, 18], [4, 18], [5, 18], [5, 17], [5, 16], [4, 16],
                  [3, 16], [2, 16], [2, 14], [3, 14], [4, 14], [5, 14], [6, 14], [7, 14], [7, 15], [7, 16], [7, 17],
                  [7, 18], [7, 19], [7, 20], [2, 12], [3, 12], [3, 11], [3, 10], [2, 10], [2, 9], [2, 8], [2, 7],
                  [2, 6], [2, 5], [2, 4], [2, 3], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2],
                  [10, 2], [11, 2], [11, 3], [11, 4], [11, 5], [11, 6], [12, 6], [13, 6], [13, 5], [13, 4], [13, 3],
                  [13, 2], [14, 2], [15, 2], [16, 2], [17, 2], [18, 2], [18, 1], [18, 3], [18, 4], [17, 4], [16, 4],
                  [15, 4], [15, 5], [15, 6], [16, 6], [17, 6], [18, 6], [18, 7], [18, 8], [17, 8], [16, 8], [15, 8],
                  [14, 8], [13, 8], [6, 6], [7, 6], [7, 7], [7, 8], [7, 9], [7, 10], [7, 11], [7, 12], [6, 12], [5, 12],
                  [5, 11], [5, 10], [5, 9], [5, 8], [4, 8], [4, 7], [4, 6], [4, 5], [4, 4], [5, 4], [6, 4], [7, 4],
                  [8, 4], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [10, 8], [11, 8], [11, 9], [11, 10], [12, 10],
                  [13, 10], [14, 10], [15, 10], [16, 10], [17, 10], [18, 10], [19, 10], [5, 12], [6, 12], [7, 12],
                  [8, 12], [9, 12], [9, 10], [9, 11], [9, 12], [9, 13], [9, 14], [9, 15], [9, 16], [9, 17], [9, 18],
                  [10, 18], [11, 18], [13, 18], [13, 19], [11, 17], [11, 16], [11, 15], [11, 14], [11, 13], [11, 12],
                  [12, 12], [13, 12], [14, 12], [15, 12], [16, 12], [17, 12], [18, 12], [18, 13], [18, 14], [17, 14],
                  [16, 14], [15, 14], [14, 14], [13, 14], [12, 16], [13, 16], [14, 16], [15, 16], [15, 17], [15, 18],
                  [16, 18], [17, 18], [18, 18], [18, 17], [18, 16], [17, 16]]
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

        for i in range(4):
            x = newX + newPiece.x(i)
            y = newY - newPiece.y(i)
            if x < 0 or x >= Board.BoardW or y < 0 or y >= Board.BoardH or [x, y] in self.a:
                return False
        print(newX, newY)
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
