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
        self.begin.clicked.connect(self.Run)
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
    """
        def paintEvent(self,e):

        qp = QPainter()
        qp.begin(self)
        qp.setPen(Qt.black)
        qp.setPen(Qt.SolidLine)
        #self.graphicsView.drawFrame(qp)
        qp.drawLine(10, 10, 30, 30)
        qp.end()
    """

    def line_arc41Compute(self):
        linex1 = float(self.linearc1_x1.text())
        linex2 = float(self.linearc1_x2.text())
        liney1 = float(self.linearc1_y1.text())
        liney2 = float(self.linearc1_y2.text())
        arcxo = float(self.linearc2_xo.text())
        arcyo = float(self.linearc2_yo.text())
        arcx2 = float(self.linearc2_x2.text())
        arcy2 = float(self.linearc2_y2.text())
        offset = float(self.rd.text())

        #直线和X轴的夹角 直线起点终点不能相同
        cosa1 = (linex2 -linex1)/\
                ((linex2 - linex1 )**2+(liney2 -liney1)**2)**0.5
        #直线和Y轴夹角
        sina1=(liney2-liney1)/\
           ((linex2-linex1)**2+(liney2-liney1)**2)**0.5
        #起点xy 表示为xa ya
        xa=linex1-offset*sina1
        ya=liney1+offset*cosa1
        #圆弧的半径
        R=((arcxo-linex2)**2+(arcyo-liney2)**2)**0.5
        #偏置向量
        xA= xa - linex1
        yA= ya - liney1
        #直线向量
        xA1 = linex2 - linex1
        yA1 = liney2 - liney1
        ############################################################### 分母等于0会程序出错
        if linex1>linex2:
            xB = -1/(((arcyo-liney2)/(arcxo-linex2))**2+1)**0.5
        elif linex1<linex2:
            xB = 1 / (((arcyo - liney2) / (arcxo - linex2)) ** 2 + 1) ** 0.5
        elif liney1>liney2:
            xB = -1 / (((arcyo - liney2) / (arcxo - linex2)) ** 2 + 1) ** 0.5
        else:
            xB = 1 / (((arcyo - liney2) / (arcxo - linex2)) ** 2 + 1) ** 0.5
        yB=((arcyo - liney2) / ( arcxo - linex2))*xB
        ################################################################
        xd=xB+linex2
        yd=yB+liney2
        #xd是直线终点在往圆弧切线方向运动单位向量的长度的点
        cosx=(xB*xA+yB*yA)/offset #切线与偏置方向的夹角
        if cosx <= 0:
            #A'B'和x轴y轴的夹角
            sina=sina1
            cosa=cosa1
            #OA‘和x轴y轴的夹角
            sinb=(arcyo-ya)/((arcxo-xa)**2+(arcyo-ya)**2)**0.5
            cosb=(arcxo-xa)/((arcxo-xa)**2+(arcyo-ya)**2)**0.5
            cosB_A_O =cosa*cosb+sina*sinb #B'A'O的夹角cos
            #AO直线长度
            AO=((arcyo-ya)**2+(arcxo-xa)**2)**0.5
            #A’B‘直线长度
            AB=AO*cosB_A_O + ((R+offset)**2+(AO**2)*(cosB_A_O**2-1))**0.5
            #表示的A'B' xy分量
            ABx=AB*cosa
            ABy=AB*sina
            #B点
            xb=xa+ABx
            yb=ya+ABy
            #OC’和XY轴的夹角
            cosa2=(arcx2-arcxo)/ \
                  ((arcx2-arcxo)**2+(arcyo-arcy2)**2)**0.5
            sina2=(arcyo-arcy2)/ \
                   ((arcx2-arcxo)**2+(arcyo-arcy2)**2)**0.5

            xc=arcx2+offset*cosa2
            yc=arcy2-offset*sina2
            print(xa,ya,xb,yb,xc,yc)
            QMessageBox.information(self,"结果",str(xa)+","+str(ya)+","+str(xb)+","+str(yb)+","+str(xc)+","+str(yc))
            ##########################情况1缩短型，输出3个点直线起点、圆弧的起点、圆弧的中点
        else:

            coso=(xA1*xB+yA1*yB)/(xA1**2+yA1**2)**0.5
            if coso >= 0:
                Sina2=(yd-liney2)/((xd-linex2)**2+(yd-liney2)**2)**0.5
                Cosa2=(xd-linex2)/((xd-linex2)**2+(yd-liney2)**2)**0.5
                xb=linex2-offset*((sina1+Sina2)/(1+Cosa2*cosa1+Sina2*sina1))
                yb=liney2-offset*((-cosa1-Cosa2)/(1+Cosa2*cosa1+Sina2*sina1))
                #####################我看不懂啊 B点！！！！
                sina3=(arcyo-liney2)/ \
                  ((arcxo-linex2)**2+(arcyo-liney2)**2)**0.5
                cosa3=(arcxo-linex2)/ \
                  ((arcxo-linex2)**2+(arcyo-liney2)**2)**0.5
                #C点计算
                xc=linex2+offset*cosa3
                yc=liney2+offset*sina3
                cosa2 = (arcx2 - arcxo) / \
                  ((arcx2 - arcxo)**2+(arcyo - arcy2)**2)**0.5
                sina2 = (arcyo - arcy2) / \
                  ((arcx2-arcxo) ** 2+(arcyo-arcy2)**2)**0.5
                #E点计算
                xe = arcx2 + offset * cosa2
                ye = arcy2 - offset * sina2

                print(xa,ya,xb,yb,xc,yc,xe,ye)
                QMessageBox.information(self, "结果", str(xa) + "," + str(ya) +
                                        "," + str(xb) + "," + str(yb) + "," +
                                        str(xc) + "," + str(yc)+","+str(xe)+","+str(ye))
                ############伸长型
            else:
                #BC点
                Sina2 = (yd - liney2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                Cosa2 = (xd - linex2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                xb = linex2 + offset * (cosa1-sina1)
                yb = liney2 + offset * (cosa1+sina1)
                xc= linex2 + offset * (-Sina2-Cosa2)
                yc=liney2 + offset * (-Sina2+Cosa2)

                #EF点的计算
                sina3 = (arcyo - liney2) / \
                 ((arcxo - linex2)**2+(arcyo - liney2)**2)**0.5
                cosa3 = (arcxo - linex2) / \
                 ((arcxo - linex2)**2+(arcyo-liney2)**2)**0.5
                xe = linex2 + offset * cosa3
                ye = liney2 + offset * sina3
                cosa2 = (arcx2 - arcxo) / \
                  ((arcx2 -arcxo)**2+(arcyo - arcy2)**2)**0.5
                sina2 = (arcyo- arcy2) / \
                   ((arcx2- arcxo) **2+(arcyo-arcy2)**2)**0.5
                xf = arcx2 + offset * cosa2
                yf = arcy2 - offset * sina2
                print(xa, ya, xb, yb, xc, yc, xe, ye, xf, yf)
                QMessageBox.information(self, "结果", str(xa) + "," + str(ya) +
                                        "," + str(xb) + "," + str(yb) + "," +
                                        str(xc) + "," + str(yc)+","+str(xe)+","+str(ye)+","
                                        + str(xf)+","+str(yf))
                ######插入型的
                #return xa,ya,xb,yb,xc,yc,xe,ye,xf,yf



    #另一个老八
    """
        def line_arc42Compute(self):
        cosa1 = (linex2 - linex1)/\
                ((linex2 - linex1)**2 +(liney2-liney1)**2)**0.5
        sina1 = (liney2 - liney1) /\
                ((linex2 - linex1)**2 +(liney2-liney1)**2)**0.5
        xa = linex1 + offset * sina1
        ya = liney1 - offset * cosa1
        R = ((self.linearc_x0.text - linex2) ** 2 + (self.linearc_y0.text - liney2)**2)** 0.5
        xA = xa - linex1
        yA = ya - linex2
        xA1 = self.linearc1_x2 - self.linearc1_x1
        yA1 = self.linearc1_y2 - self.linearc1_y1
        if self.linearc1_x1 > self.linearc1_x2:
            xB = -1 / (((self.linearc_yo.text - liney2) / (
                        self.linearc_xo.text - linex2)) ** 2 + 1) ** 0.5
        elif self.linearc1_x1 < self.linearc1_x2:
            xB = 1 / (((self.linearc_yo.text - liney2) / (
                    self.linearc_xo.text - linex2)) ** 2 + 1) ** 0.5
        elif self.linearc1_y1 > self.linearc1_y2:
            xB = -1 / (((self.linearc_yo.text - liney2) / (
                    self.linearc_xo.text - linex2)) ** 2 + 1) ** 0.5
        else:
            xB = 1 / (((self.linearc_yo.text - liney2) / (
                    self.linearc_xo.text - linex2)) ** 2 + 1) ** 0.5
        yB = ((self.linearc_yo.text - liney2) / (
                self.linearc_xo.text - linex2)) * xB
        xd = xB + linex2
        yd = yB + liney2
        cosx = (xB * xA + yB * yA) / R  # 切线与偏置方向的夹角
        if cosx >= 0:
            sina = sina1
            cosa = cosa1
            sinb = (self.linearc_yo.text - ya) / (
                        (self.linearc_xo.text - xa) ** 2 + (self.linearc_yo.text - ya) ** 2) ** 0.5
            cosb = (self.linearc_xo.text - xa) / (
                        (self.linearc_xo.text - xa) ** 2 + (self.linearc_yo.text - ya) ** 2) ** 0.5
            coy = cosa * cosb + sina * sinb
            AO = ((self.linearc_yo.text - ya) ** 2 + (self.linearc_xo.text - xa) ** 2) ** 0.5
            AB = AO * coy + ((R + offset) ** 2 - (AO ** 2) * (coy ** 2 - 1)) ** 0.5
            ABx = AB * cosa
            ABy = AB * sina
            xb = xa + ABx
            yb = ya + ABy
            cosa2 = (arcx2.text - self.linearc_xo.text) / \
                    ((arcx2.text - self.linearc_xo.text) ** 2 + (
                                self.linearc_yo.text - arcy2) ** 2) ** 0.5
            sina2 = (self.linearc_yo.text - arcy2) / \
                    ((arcx2.text - self.linearc_xo.text) ** 2 + (
                                self.linearc_yo.text - arcy2) ** 2) ** 0.5
            xc = arcx2 - offset * cosa2
            yc = arcy2 + offset * sina2
    
    
        else:
            coso = (xA1 * xB + yA1 * yB) / (xA1 ** 2 + yA1 ** 2) ** 0.5
            if coso >= 0:
                Sina2 = (yd - liney2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                Cosa2 = (xd - linex2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                xb = linex2 + offset * ((sina1 + Sina2) / (1 + Cosa2 * cosa1 + Sina2 * sina1))
                yb = liney2 + offset * ((-cosa1 - Cosa2) / (1 + Cosa2 * cosa1 + Sina2 * sina1))
                sina3 = (self.linearc_yo.text - liney2) / \
                 ((self.linearc_xo.text - linex2) ** 2+(self.linearc_yo.text-liney2)**2)**0.5
                cosa3 = (self.linearc_xo.text - linex2) / \
                   ((self.linearc_xo.text - linex2)**2+(self.linearc_yo.text-liney2)**2)**0.5
                xc = linex2 + offset * cosa3
                yc = liney2 + offset * sina3
                cosa2 = (arcx2.text - self.linearc_xo.text) / \
                   ((arcx2.text - self.linearc_xo.text)**2+(self.linearc_yo.text - arcy2)**2)**0.5
                sina2 = (self.linearc_yo.text - arcy2) / \
                   ((arcx2.text - self.linearc_xo.text) ** 2+(self.linearc_yo.text-arcy2)**2)**0.5
                xe = arcx2 - offset * cosa2
                ye = arcy2 + offset * sina2
    
            else:
                Sina2 = (yd - liney2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                Cosa2 = (xd - linex2) / \
                        ((xd - linex2) ** 2 + (yd - liney2) ** 2) ** 0.5
                xb = linex2 + offset * (sina1+Cosa2)
                yb = liney2 + offset * (sina1-cosa1)
                xc = linex2 + offset * (Sina2-Cosa2)
                yc = liney2 + offset * (-Cosa2 - Sina2)
                sina3 = (self.linearc_yo.text - liney2) / \
                        ((self.linearc_xo.text - linex2) ** 2 + (
                                    self.linearc_yo.text - liney2) ** 2) ** 0.5
                cosa3 = (self.linearc_xo.text - linex2) / \
                        ((self.linearc_xo.text - linex2) ** 2 + (
                                    self.linearc_yo.text - liney2) ** 2) ** 0.5
                xe = linex2 + offset * cosa3
                ye = liney2 + offset * sina3
                cosa2 = (arcx2.text - self.linearc_xo.text) / \
                        ((arcx2.text - self.linearc_xo.text) ** 2 + (
                                    self.linearc_yo.text - arcy2) ** 2) ** 0.5
                sina2 = (self.linearc_yo.text - arcy2) / \
                        ((arcx2.text - self.linearc_xo.text) ** 2 + (
                                    self.linearc_yo.text - arcy2) ** 2) ** 0.5
                xf = arcx2 - offset * cosa2
                yf = arcy2 + offset * sina2
        #return xa, ya, xb, yb, xc, yc, xe, ye, xf, yf
        print(xa, ya, xb, yb, xc, yc, xe, ye, xf, yf)
    """



    def Run(self):
        self.line_arc41Compute()


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


    """
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
    """



if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show();
    sys.exit(app.exec_())