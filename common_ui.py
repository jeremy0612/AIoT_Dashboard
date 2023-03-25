from PyQt5.QtWidgets import QMainWindow ,QApplication, QVBoxLayout
from PyQt5 import uic,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sys

class MainWindow(QMainWindow):
	"""docstring for MainWindow"""
	def __init__(self, arg):
		super().__init__()
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.moveFlag = True
			self.movePosition = event.globalPos() - self.pos()
			event.accept()
	def mouseMoveEvent(self, event):
		mouse_x,mouse_y = QCursor.pos().x(),QCursor.pos().y()
		geometry = self.geometry()
		x,y,_,_ = geometry.getCoords()
		#print("App position:{} {}\nMouse position:{} {}".format(x,y,mouse_x,mouse_y))
		if Qt.LeftButton and self.moveFlag:
			if mouse_y-y in range(60): 
				self.setCursor(QCursor(Qt.OpenHandCursor))
				self.move(event.globalPos() - self.movePosition)
				event.accept()
				
	def mouseReleaseEvent(self, event):
		self.moveFlag = False
		self.setCursor(Qt.ArrowCursor) #IBeamCursor/CrossCursor	
		