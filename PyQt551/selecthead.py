# -*- coding: utf-8 -*-

"""
Module implementing SelectHead.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from selectsexy import SelectSexy
from Ui_head import Ui_Form


class SelectHead(QWidget, Ui_Form):

    man_or_feman = ""
    head = "0"

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectHead, self).__init__(parent)
        self.setupUi(self)
    