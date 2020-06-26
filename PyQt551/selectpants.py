# -*- coding: utf-8 -*-

"""
Module implementing SelectPants.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_pants import Ui_Form


class SelectPants(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SelectPants, self).__init__(parent)
        self.setupUi(self)
    
    