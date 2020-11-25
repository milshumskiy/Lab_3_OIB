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

def openFullSize(imPath):
	if imPath:
		if platform.system() == 'Darwin':       # macOS
			try:
				subprocess.call(('open', imPath))
				addToLog('# FILE  \''+ imPath + '\' WAS OPENED AT FULL SIZE')
			except OSError:
				addToLog('# ERROR: UNCNOWN ERROR')
		elif platform.system() == 'Windows':    # Windows
			try:
				subprocess.call(imPath, shell=True)
				addToLog('# FILE  \''+ imPath + '\' WAS OPENED AT FULL SIZE')
			except OSError:
				addToLog('# ERROR: UNCNOWN ERROR')
		else:                                   # linux variants
			try:
				subprocess.call(('xdg-open', imPath))
				addToLog('# FILE  \''+ imPath + '\' WAS OPENED AT FULL SIZE')
			except OSError:
				addToLog('# ERROR: UNCNOWN ERROR')
	

def getImage():
	global im
	global imagePath
	if not imagePath:
		qfd = QFileDialog()
		fName = QFileDialog.getOpenFileName(qfd, 'Open File', '', 'Images (*.png *.jpg *.bmp)')
		imagePath = fName[0]
		im = imagePath
		if imagePath:
			showImage(imagePath)
			addToLog('# FILE WAS SELECTED: ' + imagePath)
	else:
		tempPath = imagePath
		qfd = QFileDialog()
		fName = QFileDialog.getOpenFileName(qfd, 'Open File', '', 'Images (*.png *.jpg *.bmp)')
		imagePath = fName[0]
		im = imagePath
		if imagePath:
			showImage(imagePath)
			addToLog('# FILE WAS SELECTED: ' + imagePath)
		else:
			imagePath = tempPath
			im = imagePath


def showImage(pathF):
	if pathF:
		pixmap = QPixmap(pathF)
		ui.label.setScaledContents(True)
		ui.label.setPixmap(QPixmap(pixmap))

def addToLog(text):
	ui.textBrowser.append(text)
	logFile.write(text + '\n')

def start_button():
	global im
	if imagePath:
		addToLog('# IMAGE \'' + imagePath + '\' HAS BEEN SENT FOR PROCESSING......')
		im = get_watermark_image(imagePath)
		if im == '1001':
			addToLog('# ERROR: HTTP ERROR')
		elif im == '1002':
			addToLog('# ERROR: ERROR CONNECTING')
		elif im == '1003':
			addToLog('# ERROR: TIMEOUT ERROR')
		elif im == '1004':
			addToLog('# ERROR: INTERNAL SERVER ERROR')
		else:
			try:
				save_image(im)
			except IOError:
				addToLog('# ERROR: NO SUCH FILE OR DIRECTORY')
			except BaseException:
				addToLog('# ERROR: INTERNAL SERVER ERROR')
			else:
				addToLog('# IMAGE \'' + imagePath + '\' PROCESSED SUCCESSFULLY')
				im = 'Processed image.png'
				showImage(im)
	else:
		addToLog('# ERROR: FILE NOT SELECTED')

ui.pushButton.clicked.connect(getImage)
ui.pushButton_2.clicked.connect(start_button)
clickable(ui.label).connect(lambda: openFullSize(im))

# Main loop
sys.exit(app.exec_())