from PyQt5.QtWidgets import QMainWindow ,QApplication, QVBoxLayout
from PyQt5 import uic,QtCore
from PyQt5.QtCore import QTimer,QDateTime,Qt
from PyQt5.QtGui import QCursor
from common_ui import *
from chart import Piechart,Barchart,Linechart,Donutchart,Scatterchart
import sys


class MAIN_menu(MainWindow):
	def __init__(self):
		#---------------------Set status---------------------------------
		super().__init__(self)
		uic.loadUi("UI/dialog.ui",self)
		self.normal_shown = True
		self.pie_chart = Piechart()
		self.bar_chart = Barchart()
		self.line_chart = Linechart()
		self.donut_chart = Donutchart()
		self.scatter_chart = Scatterchart()
		
		self.chart_timer = QTimer()
		self.chart_timer.timeout.connect(lambda: self.update_chart('1'))
		self.chart_timer.start(17000)

		self.chart_timer_2 = QTimer()
		self.chart_timer_2.timeout.connect(lambda: self.update_chart('2'))
		self.chart_timer_2.start(7000)

		self.exe_timer = QTimer()
		self.exe_timer.timeout.connect(lambda: self.current_time.setText(QDateTime.currentDateTime().toString('yyyy-MM-dd hh:mm:ss dddd')))
		self.exe_timer.start(1000)

		#===============================================================

		#------------------ Size control buttons-------------------------
		self.close_button.clicked.connect(lambda: self.close())
		self.minimize_button.clicked.connect(lambda: self.showMinimized())
		self.maximize_button.clicked.connect(lambda: self.Full_scr())
		#self.line_chart_button.clicked.connect(lambda: self.Set_up_chart("linechart"))
		#self.bar_chart_button.clicked.connect(lambda: self.Set_up_chart("barchart"))
		
		#=================================================================
	
		#------------------BUTTON----------------------------------------
		self.bar_chart_button.clicked.connect(lambda: self.main_content.setCurrentWidget(self.barchart))
		self.line_chart_button.clicked.connect(lambda: self.main_content.setCurrentWidget(self.linechart))
		self.pie_chart_button.clicked.connect(lambda: self.main_content.setCurrentWidget(self.piechart))
		self.donut_chart_button.clicked.connect(lambda: self.main_content.setCurrentWidget(self.donutchart))
		self.scatter_chart_button.clicked.connect(lambda: self.main_content.setCurrentWidget(self.scatterchart))
		self		

		#================================================================

		#------------------Data analyst menu-----------------------------
		self.more_menu_status = [0,False,False,False,False,False,False]
							  #  sta,data,report,setting,inform,help,home,close 
		self.data_button.clicked.connect(lambda: self.more_menu(1))
		self.report_button.clicked.connect(lambda: self.more_menu(2))
		self.setting_button.clicked.connect(lambda: self.more_menu(3))
		self.inform_button.clicked.connect(lambda: self.more_menu(4))
		self.help_button.clicked.connect(lambda: self.more_menu(5))
		self.home_button.clicked.connect(lambda: self.more_menu(6))
		self.close_menu_button.clicked.connect(lambda: self.more_menu(7))
		print(self.more_menu_status)
		#================================================================
		
		self.Set_up_UI()
	def update_chart(self,_a):
		print("updating")
		if _a=='1':
			self.line_chart.chart.removeAllSeries()
			self.line_chart.update_data()
			self.line_chart.chart.addSeries(self.line_chart.series)
		else:
			self.scatter_chart.chart.removeAllSeries()
			self.scatter_chart.update_data()
			self.scatter_chart.chart.addSeries(self.scatter_chart.series)
	def deleteItems(self,layout):
             if layout is not None:
                 while layout.count():
                     item = layout.takeAt(0)
                     widget = item.widget()
                     if widget is not None:                  
                         widget.deleteLater()
                     else:
                         deleteItems(item.layout())
	def more_menu(self,b):
		if self.more_menu_status[0]!=0 and b==7:
			self.stackedWidget.setVisible(False) 
			self.frame_4.setVisible(False)
			self.more_menu_status[0] = 0
			self.data_button.setStyleSheet("")
			self.report_button.setStyleSheet("")
			self.help_button.setStyleSheet("")
			self.help_button.setStyleSheet("")
			self.inform_button.setStyleSheet("")
			self.home_button.setStyleSheet("")
			self.setting_button.setStyleSheet("")
		else:
			self.frame_4.setVisible(True)
			self.stackedWidget.setVisible(True)
			for i in range(1,7):
				self.more_menu_status[i]=False
			if b==1 :
				self.stackedWidget.setCurrentWidget(self.data_menu) 
				self.more_menu_status[1] = True
				self.more_menu_status[0] = b 
				self.data_button.setStyleSheet("background-color: #1f232a;")
			elif b==2:
				self.stackedWidget.setCurrentWidget(self.report_menu) 
				self.more_menu_status[2] = True
				self.more_menu_status[0] = b
				self.report_button.setStyleSheet("background-color: #1f232a;")
			elif b==3 :
				self.stackedWidget.setCurrentWidget(self.setting_menu) 
				self.more_menu_status[3] = True
				self.more_menu_status[0] = b
				self.setting_button.setStyleSheet("background-color: #1f232a;")
			elif b==4 :
				self.stackedWidget.setCurrentWidget(self.inform_menu) 
				self.more_menu_status[4] = True
				self.more_menu_status[0] = b
				self.inform_button.setStyleSheet("background-color: #1f232a;")
			elif b==5 :
				self.stackedWidget.setCurrentWidget(self.help_menu) 
				self.more_menu_status[5] = True
				self.more_menu_status[0] = b
				self.help_button.setStyleSheet("background-color: #1f232a;")
			elif b==6 :
				self.stackedWidget.setCurrentWidget(self.home_menu) 
				self.more_menu_status[6] = True
				self.more_menu_status[0] = b
				self.home_button.setStyleSheet("background-color: #1f232a;")
		#print(self.more_menu_status)	#debug
			

	def Full_scr(self):
		if self.normal_shown==True:
			self.showMaximized()
			self.normal_shown = False
		else:
			self.showNormal()
			self.normal_shown = True

	def Set_up_UI(self):
		self.stackedWidget.setVisible(False) 
		self.frame_4.setVisible(False)
		self.Set_up_chart()
	def Set_up_chart(self):
		self.linechart.setLayout(self.line_chart.vbox)
		self.barchart.setLayout(self.bar_chart.vbox)
		self.piechart.setLayout(self.pie_chart.vbox)
		self.donutchart.setLayout(self.donut_chart.vbox)
		self.scatterchart.setLayout(self.scatter_chart.vbox)

		
		#self.main_body_content.setLayout(self.pie_chart.vbox)

	

if __name__ == '__main__':
	app = QApplication(sys.argv)
	
	main = MAIN_menu()
	main.show()
	
	sys.exit(app.exec_())