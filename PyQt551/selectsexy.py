# -*- coding: utf-8 -*-

"""
Module implementing SelectSexy.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPixmap

from Ui_sexy import Ui_Form


class SelectSexy(QWidget, Ui_Form):

    # sexy = ""

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectSexy, self).__init__(parent)
        self.setupUi(self)
    
