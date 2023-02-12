from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
from main import MAIN_menu
from login import LOGIN_menu, SIGNUP_menu
from sheet_data import USER_DATA,DEVICE_DATA
from PyQt5 import QtCore 
from PyQt5.QtCore import QTimer
import sys


class APP():
	def __init__(self):
		#------------Init app elements--------------#
		self.user = USER()
		self.login = LOGIN_menu()	
		self.signup = SIGNUP_menu()
		self.login.show()

		#===========================================
		
		#---------------- Login button/log out button and sign up button------------------------------
		self.login.confirm_button.clicked.connect(self.Check_inform)
		self.login.signup_button.clicked.connect(lambda: self.Change_intro_UI("log in"))
		self.login.close_button.clicked.connect(lambda: self.login.close())
		self.login.minimize_button.clicked.connect(lambda: self.login.showMinimized())
		self.signup.back_button.clicked.connect(lambda: self.Change_intro_UI("sign up"))
		#================================================================================

	def Check_inform(self):
		print("Checking inform .....")
		self.user.name = self.login.lineEdit1.text()
		self.user.password = self.login.lineEdit2.text()
		print("User name:",self.user.name,"| Password:",self.user.password)
		if self.user.Check_data() == True:
			self.start()
		else:
			self.login.label.setText("   WRONG ACCOUNT!")
  	
  	#def Add_user(self):
  		

	def Change_intro_UI(self,a):
		if a == "log in":
			#self.login.showMinimized()
			#self.login.close()
			self.login.hide()
			self.signup.show()
		elif a == "sign up":
			self.signup.hide()
			self.login.show()
   
	def log_out(self):
		self.main.close()
		self.login.show()
	def start(self):
		self.main = MAIN_menu()
		self.login.close()
		self.main.show()


class USER(USER_DATA):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.password = ""
        self.email = ""
    def Check_data(self):
        print("checking....")
        for i in self.values:
            if self.name == i[0] and self.password == i[1]:
                print("account is valid")
                return True
        print("account is invalid")
            

if __name__ == "__main__":
	app = QApplication(sys.argv)
	
	This_app = APP()
	#main_menu = Example_menu()

	sys.exit(app.exec_())









	