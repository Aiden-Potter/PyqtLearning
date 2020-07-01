from PyQt5.QtWidgets import QPushButton, QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie


class MsgBox(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowFlags(Qt.Tool)
        self.resize(450,300)
        self.setWindowTitle('宝贝，亲一个！')
        bt = QPushButton('好的！',self)
        bt.setDefault(True)
        label = QLabel(self)
        movie = QMovie("tianpin.gif")
        label.setMovie(movie)
        movie.start()
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(bt)
        hbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.show()
        bt.clicked.connect(self.ok)

    def ok(self):
        self.done(1) 
