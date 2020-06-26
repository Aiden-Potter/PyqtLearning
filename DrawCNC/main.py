from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from ks3 import Ui_Form

class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self,parent = None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.tabWidget.setTabEnabled(0,True)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.pushButton_line_line.clicked.connect(self.ChangeToLineLine)
        self.pushButton_line_arc.clicked.connect(self.ChangeToLineArc)
        self.pushButton_arc_line.clicked.connect(self.ChangeToArcLine)
        self.pushButton_arc_arc.clicked.connect(self.ChangeToArcArc)

        """
        mainSplitter1 = QSplitter(Qt.Horizontal)
        mainSplitter1.setOpaqueResize(True)
        stack1 = QStackedWidget()
        stack1.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.area = PaintArea()
        stack1.addWidget(self.area)
        frame1 = QFrame(mainSplitter1)
        mainLayout1 = QVBoxLayout(frame1)
        # mainLayout1.setMargin(10)
        mainLayout1.setSpacing(6)
        mainLayout1.addWidget(stack1)
        layout = QGridLayout(self)
        layout.addWidget(mainSplitter1, 0, 0)
        #layout.addWidget(self.mainSplitter, 0, 1)
        self.setLayout(layout)
        """

    def paintEvent(self,e):

        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.black)
        qp.setPen(Qt.SolidLine)
        #self.graphicsView.drawFrame(qp)
        qp.drawLine(10, 10, 30, 30)
        qp.end()



    def ChangeToLineLine(self):
        self.tabWidget.setTabEnabled(0,True)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setCurrentIndex(0)

    def ChangeToLineArc(self):
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,True)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setCurrentIndex(1)
    def ChangeToArcLine(self):
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,True)
        self.tabWidget.setTabEnabled(3,False)
        self.tabWidget.setCurrentIndex(2)
    def ChangeToArcArc(self):
        self.tabWidget.setTabEnabled(0,False)
        self.tabWidget.setTabEnabled(1,False)
        self.tabWidget.setTabEnabled(2,False)
        self.tabWidget.setTabEnabled(3,True)
        self.tabWidget.setCurrentIndex(3)

class PaintArea(QWidget):
    def __init__(self):
        super(PaintArea, self).__init__()
        self.Shape = ["Line", "Rectangle", 'Rounded Rectangle', "Ellipse", "Pie", 'Chord',
                      "Path", "Polygon", "Polyline", "Arc", "Points", "Text", "Pixmap"]
        self.setPalette(QPalette(Qt.white))
        self.setAutoFillBackground(True)
        self.setMinimumSize(400, 400)
        self.pen = QPen()
        self.brush = QBrush()

    def setShape(self, s):
        self.shape = s
        self.update()

    def setPen(self, p):
        self.pen = p
        self.update()

    def setBrush(self, b):
        self.brush = b
        self.update()

    def paintEvent(self, QPaintEvent):
        p = QPainter(self)
        p.setPen(self.pen)
        p.setBrush(self.brush)

        rect = QRect(50, 100, 300, 200)
        points = [QPoint(150, 100), QPoint(300, 150), QPoint(350, 250), QPoint(100, 300)]
        startAngle = 30 * 16
        spanAngle = 120 * 16

        path = QPainterPath();
        path.addRect(150, 150, 100, 100)
        path.moveTo(100, 100)
        path.cubicTo(300, 100, 200, 200, 300, 300)
        path.cubicTo(100, 300, 200, 200, 100, 100)
        if self.shape == "Line":
            p.drawLine(rect.topLeft(), rect.bottomRight())
        elif self.shape == "Rectangle":
            p.drawRect(rect)
        elif self.shape == 'Rounded Rectangle':
            p.drawRoundedRect(rect, 25, 25, Qt.RelativeSize)
        elif self.shape == "Ellipse":
            p.drawEllipse(rect)
        elif self.shape == "Polygon":
            p.drawPolygon(QPolygon(points), Qt.WindingFill)
        elif self.shape == "Polyline":
            p.drawPolyline(QPolygon(points))
        elif self.shape == "Points":
            p.drawPoints(QPolygon(points))
        elif self.shape == "Pie":
            p.drawPie(rect, startAngle, spanAngle)
        elif self.shape == "Arc":
            p.drawArc(rect, startAngle, spanAngle)
        elif self.shape == "Chord":
            p.drawChord(rect, startAngle, spanAngle)
        elif self.shape == "Path":
            p.drawPath(path)
        elif self.shape == "Text":
            p.drawText(rect, Qt.AlignCenter, "Hello Qt!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show();
    sys.exit(app.exec_())