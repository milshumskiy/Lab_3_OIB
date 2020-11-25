import sys, os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLabel, QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap
from watermark import Ui_Dialog
import subprocess, os, platform
from datetime import datetime
from client import *

sys.path.append("pyqt path")

# Create app
app = QtWidgets.QApplication(sys.argv)

# init
#Dialog = QtWidgets.QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.Window)
Dialog = QtWidgets.QDialog()
Dialog.setWindowFlags(Dialog.windowFlags() | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowSystemMenuHint)
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()

# Hool logic
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
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
            
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

def openFullSize():
	if platform.system() == 'Darwin':       # macOS
		try:
			subprocess.call(('open', imagePath))
			addToLog('# FILE  \''+ imagePath + '\' WAS OPENED AT FULL SIZE')
		except OSError:
			addToLog('# ERROR: ')
	elif platform.system() == 'Windows':    # Windows
		try:
			#os.startfile(r'D:\\kozmonaut-181918.jpg')
			subprocess.call(imagePath, shell=True)
			addToLog('# FILE  \''+ imagePath + '\' WAS OPENED AT FULL SIZE')
		except OSError:
			addToLog('# ERROR: ')
	else:                                   # linux variants
		try:
			subprocess.call(('xdg-open', imagePath))
			addToLog('# FILE  \''+ imagePath + '\' WAS OPENED AT FULL SIZE')
		except OSError:
			addToLog('# ERROR: ')
	

def getImage():
	qfd = QFileDialog()
	fName = QFileDialog.getOpenFileName(qfd, 'Open File', '', 'Images (*.png *.xpm *.jpg *.bmp *.ico)')
	global imagePath
	imagePath = fName[0]

	pixmap = QPixmap(imagePath)
	ui.label.setScaledContents(True);
	ui.label.setPixmap(QPixmap(pixmap))
	addToLog('# FILE WAS SELECTED: ' + imagePath)

def addToLog(text):
	ui.textBrowser.append(text)
	logFile.write(text)

def createLogFile():
	pass

ui.pushButton.clicked.connect(getImage)
ui.pushButton_2.clicked.connect(lambda: save_image(get_watermark_image(imagePath)))
clickable(ui.label).connect(openFullSize)

# Main loop
sys.exit(app.exec_())