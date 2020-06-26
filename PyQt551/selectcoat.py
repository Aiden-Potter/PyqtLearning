# -*- coding: utf-8 -*-

"""
Module implementing SelectCoat.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from Ui_coat import Ui_Form


class SelectCoat(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectCoat, self).__init__(parent)
        self.setupUi(self)
    
    