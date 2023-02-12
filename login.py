from PyQt5.QtWidgets import QMainWindow 
from PyQt5 import uic,QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
import sys

class LOGIN_menu(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("UI/login.ui",self)
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.moveFlag = True
			self.movePosition = event.globalPos() - self.pos()
			self.setCursor(QCursor(Qt.OpenHandCursor))
			event.accept()
	def mouseMoveEvent(self, event):
		if Qt.LeftButton and self.moveFlag:
			self.move(event.globalPos() - self.movePosition)
			event.accept()
	def mouseReleaseEvent(self, event):
		self.moveFlag = False
		self.setCursor(Qt.ArrowCursor) #IBeamCursor/CrossCursor
  	


class SIGNUP_menu(QMainWindow):
	def __init__(self):
		super().__init__()
		uic.loadUi("UI/signup.ui",self)
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
	def mousePressEvent(self, event):
		if event.button() == Qt.LeftButton:
			self.moveFlag = True
			self.movePosition = event.globalPos() - self.pos()
			self.setCursor(QCursor(Qt.OpenHandCursor))
			event.accept()
	def mouseMoveEvent(self, event):
		if Qt.LeftButton and self.moveFlag:
			self.move(event.globalPos() - self.movePosition)
			event.accept()
	def mouseReleaseEvent(self, event):
		self.moveFlag = False
		self.setCursor(Qt.ArrowCursor) #IBeamCursor/CrossCursor	