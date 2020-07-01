from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QLabel, QMessageBox
from PyQt5.QtCore import QRect, QPropertyAnimation, QEasingCurve, QPoint, QEvent
from MsgBox import MsgBox
import sys

class Example(QDialog):

    def __init__(self):
        super().__init__()        
        self.initUI()
        
    def initUI(self):
        
        self.resize(350,200)
        self.setWindowTitle('你爱我吗？微信公众号号：学点编程吧出品')
        self.btbuai = QPushButton("不爱", self)
        self.btai = QPushButton('爱',self)
        self.btbuai.resize(70,25)
        self.btbuai.move(200,150)
        self.btai.resize(70,25)
        self.btai.move(100,150)
        label = QLabel('你难道不爱我吗？？？？',self)
        label.move(50,50)

        self.show()
        self.flag = 'move'

        self.btai.setMouseTracking(True)
        self.btbuai.setMouseTracking(True)

        self.btai.installEventFilter(self)
        self.btbuai.installEventFilter(self)

    def eventFilter(self, object, event):
        if object == self.btbuai:
            if event.type() == QEvent.Enter:
                self.doAnim1()
        elif object == self.btai:
            if event.type() == QEvent.Enter:
                self.doAnim2()
            elif event.type() == QEvent.MouseButtonRelease:
                self.makelove()
        return QDialog.eventFilter(self, object, event)

    def closeEvent(self, event):
        QMessageBox.about(self, 'Love', '你就算关闭了窗口也阻止不了你心中对我的爱！')

    def doAnim1(self):
        if self.flag == 'move' and self.btbuai.pos() == QPoint(200, 150):
            self.anim = QPropertyAnimation(self.btbuai, b"geometry")
            self.anim.setDuration(1500)            
            self.anim.setStartValue(QRect(200, 150, 70, 25))
            self.anim.setEndValue(QRect(200, 30, 70, 25))
            self.anim.setEasingCurve(QEasingCurve.OutCubic)
            self.anim.start()
        elif self.flag == 'move' and self.btbuai.pos() == QPoint(200, 30):
                self.anim = QPropertyAnimation(self.btbuai, b"geometry")
                self.anim.setDuration(1500)
                self.anim.setStartValue(QRect(200, 30, 70, 25))
                self.anim.setEndValue(QRect(200, 150, 70, 25))
                self.anim.setEasingCurve(QEasingCurve.OutCubic)
                self.anim.start()
                self.flag = 'change'
        elif self.flag == 'change' and self.btbuai.text() == '不爱':
            self.btbuai.setText('爱')
            self.btai.setText('不爱')

    def doAnim2(self):
        if self.flag == 'change' and self.btbuai.text() == '爱':
            self.btbuai.setText('不爱')
            self.btai.setText('爱')
            self.flag = 'move'

    def makelove(self):
        msg = MsgBox()
        msg.exec()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())