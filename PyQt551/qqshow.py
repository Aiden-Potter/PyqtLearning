# -*- coding: utf-8 -*-

"""
Module implementing QQShow.
"""

from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap
from Ui_main import Ui_MainWindow
from selectsexy import SelectSexy
from selecthead import SelectHead
from selectcoat import SelectCoat
from selectpants import SelectPants

import sys

class QQShow(QMainWindow, Ui_MainWindow):
    
    sexy = ""
    head = ""
    coat = ""
    pants = ""

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(QQShow, self).__init__(parent)
        self.setupUi(self)
        self.initUi()
    
    def initUi(self):

        self.sexywidget = SelectSexy()
        self.headwidget = SelectHead()
        self.coatwidget = SelectCoat()
        self.pantswidget = SelectPants()

        self.stackedWidget.addWidget(self.sexywidget)
        self.stackedWidget.addWidget(self.headwidget)
        self.stackedWidget.addWidget(self.coatwidget)
        self.stackedWidget.addWidget(self.pantswidget)

        self.sexywidget.pushButton.clicked.connect(self.unlockhead)
        self.sexywidget.radioButton_man.toggled.connect(self.setman)
        self.sexywidget.radioButton_feman.toggled.connect(self.setfeman)

        self.headwidget.pushButton.clicked.connect(self.unlockcoat)
        self.headwidget.radioButton_head1.toggled.connect(self.sethead1)
        self.headwidget.radioButton_head2.toggled.connect(self.sethead2)
        self.headwidget.radioButton_head3.toggled.connect(self.sethead3)

        self.coatwidget.pushButton.clicked.connect(self.unlockpants)
        self.coatwidget.radioButton_coat1.toggled.connect(self.setcoat1)
        self.coatwidget.radioButton_coat2.toggled.connect(self.setcoat2)
        self.coatwidget.radioButton_coat3.toggled.connect(self.setcoat3)

        self.pantswidget.radioButton_pants1.toggled.connect(self.setpants1)
        self.pantswidget.radioButton_pants2.toggled.connect(self.setpants2)
        self.pantswidget.radioButton_pants3.toggled.connect(self.setpants3)

    
    @pyqtSlot(int)
    def on_listWidget_currentRowChanged(self, p0):
        """
        选择造型
        """
        self.stackedWidget.setCurrentIndex(p0)
    
    @pyqtSlot(int)
    def on_stackedWidget_currentChanged(self, p0):
        """
        页面切换时
        """
        if p0 == 1:
            if self.headwidget.radioButton_head1.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy + self.head + ".png"))
            elif self.headwidget.radioButton_head2.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy +  self.head + ".png"))
            elif self.headwidget.radioButton_head3.isChecked():
                self.headwidget.label.setPixmap(QPixmap(self.sexy +  self.head + ".png"))
            else:
                self.headwidget.label.setPixmap(QPixmap(self.sexy + "sexy.png"))
        elif p0 == 2:
            if self.coatwidget.radioButton_coat1.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            elif self.coatwidget.radioButton_coat2.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            elif self.coatwidget.radioButton_coat3.isChecked():
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))
            else:
                self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + ".png"))
        elif p0 == 3:
            if self.pantswidget.radioButton_pants1.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            elif self.pantswidget.radioButton_pants2.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            elif self.pantswidget.radioButton_pants3.isChecked():
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + self.pants + ".png"))
            else:
                self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + ".png"))

    def unlockhead(self):
        if self.sexywidget.radioButton_man.isChecked() or self.sexywidget.radioButton_feman.isChecked():
            QMessageBox.information(self, "提示", "头型解锁成功！")
            self.sexywidget.pushButton.setEnabled(False)
            item = self.listWidget.item(1)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        else:
            QMessageBox.information(self, "提示", "还没有选择男女呢？")    

    def setman(self):
        self.sexy = "./res/man/"
        self.sexywidget.label_sexy.setPixmap(QPixmap("./res/man/sexy.png"))

    def setfeman(self):
        self.sexy = "./res/feman/"
        self.sexywidget.label_sexy.setPixmap(QPixmap("./res/feman/sexy.png"))

    def unlockcoat(self):
        if self.headwidget.radioButton_head1.isChecked() or self.headwidget.radioButton_head2.isChecked() or self.headwidget.radioButton_head3.isChecked():
            QMessageBox.information(self, "提示", "上衣解锁成功！")
            self.headwidget.pushButton.setEnabled(False)
            item = self.listWidget.item(2)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        else:
            QMessageBox.information(self, "提示", "还没有选择头型呢？")
    
    def sethead1(self):
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "1.png"))
        self.head = "1"

    def sethead2(self):
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "2.png"))
        self.head = "2"

    def sethead3(self):
        self.headwidget.label.setPixmap(QPixmap(self.sexy + "3.png"))
        self.head = "3"

    def unlockpants(self):
        if self.coatwidget.radioButton_coat1.isChecked() or self.coatwidget.radioButton_coat2.isChecked() or self.coatwidget.radioButton_coat3.isChecked():
            QMessageBox.information(self, "提示", "裤子解锁成功！")
            self.coatwidget.pushButton.setEnabled(False)
            item = self.listWidget.item(3)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
        else:
            QMessageBox.information(self, "提示", "还没有选择上衣呢？")
    
    def setcoat1(self):
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "1.png"))
        self.coat = "1"

    def setcoat2(self):
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "2.png"))
        self.coat = "2"

    def setcoat3(self):
        self.coatwidget.label.setPixmap(QPixmap(self.sexy + self.head + "3.png"))
        self.coat = "3"

    def setpants1(self):
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "1.png"))
        self.pants = "1"

    def setpants2(self):
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "2.png"))
        self.pants = "2"

    def setpants3(self):
        self.pantswidget.label.setPixmap(QPixmap(self.sexy + self.head + self.coat + "3.png"))
        self.pants = "3"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qshow = QQShow()
    qshow.show()
    sys.exit(app.exec_())