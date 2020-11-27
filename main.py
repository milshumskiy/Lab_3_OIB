import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from watermark import Ui_Dialog
import subprocess, os, platform
import warnings
from datetime import datetime
from client import *

sys.path.append("pyqt path")
warnings.simplefilter(action='ignore', category=FutureWarning)

# Create app
app = QtWidgets.QApplication(sys.argv)

# init
Dialog = QtWidgets.QDialog()
Dialog.setWindowFlags(Dialog.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hool logic
im = ''
imagePath = ''
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d--%H-%M-%S")
logFile = open(dt_string + ".log", "w")

def clickable(widget):

    class Filter(QObject):
    
        clicked = pyqtSignal()
        
        def eventFilter(ui, obj, event):
        
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        ui.clicked.emit()
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

# Main loop
sys.exit(app.exec_())