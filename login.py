from common_ui import *
import sys

class LOGIN_menu(MainWindow):
	def __init__(self):
		super().__init__(self)
		uic.loadUi("UI/login.ui",self)
	
class SIGNUP_menu(MainWindow):
	def __init__(self):
		super().__init__(self)
		uic.loadUi("UI/signup.ui",self)
	