from PyQt5.QtWidgets import QMainWindow 
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout
from PyQt5.QtChart import QChart, QChartView, QBarSet, QPercentBarSeries, QBarCategoryAxis,QLineSeries,QPieSeries,QScatterSeries
import sys
from PyQt5.QtGui import QIcon,QPen,QPainter
from PyQt5.QtCore import Qt ,QPointF #, QObject
from sheet_data import DEVICE_DATA
import time

class Piechart():    
    def __init__(self):
        #create pieseries
        self.series  = QPieSeries()
        #append some data to the series 
        self.series.append("Apple", 80)
        self.series.append("Banana", 70)
        self.series.append("Pear", 50)
        self.series.append("Melon", 80)
        self.series.append("Water Melon", 30)
        #slice
        self.my_slice = self.series.slices()[3]
        self.my_slice.setExploded(True)
        self.my_slice.setLabelVisible(True)
        self.my_slice.setPen(QPen(Qt.green, 4))
        self.my_slice.setBrush(Qt.green)
        #create QChart object
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Fruits Pie Chart")
        self.chart.setTheme(QChart.ChartThemeDark) 
        self.chartview = QChartView(self.chart)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartview)
        
    def assign_chart(self,widget):
        self.widget.setLayout(self.vbox)

class Barchart():    
    def __init__(self):
        #create barseries
        self.set0 = QBarSet("Parwiz")
        self.set1 = QBarSet("Karim")
        self.set2 = QBarSet("Tom")
        self.set3 = QBarSet("Logan")
        self.set4 = QBarSet("Bob")
 
 
        #insert data to the barseries
        self.set0 << 1 << 2 << 3 << 4 << 5 << 6
        self.set1 << 5 << 0 << 0 << 4 << 0 << 7
        self.set2 << 3 << 5 << 8 << 13 << 8 << 5
        self.set3 << 5 << 6 << 7 << 3 << 4 << 5
        self.set4 << 9 << 7 << 5 << 3 << 1 << 2
 
        #we want to create percent bar series
        self.series = QPercentBarSeries()
        self.series.append(self.set0)
        self.series.append(self.set1)
        self.series.append(self.set2)
        self.series.append(self.set3)
        self.series.append(self.set4)
 
        #create chart and add the series in the chart
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setTitle("Barchart Percent Example")
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTheme(QChart.ChartThemeDark)
 
 
        #create axis for the chart
        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
 
        self.axis = QBarCategoryAxis()
        self.axis.append(self.categories)
        self.chart.createDefaultAxes()
        self.chart.setAxisX(self.axis, self.series)
 
        #create chartview and add the chart in the chartview
        self.chartview = QChartView(self.chart)
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartview)

        
    def assign_chart(self):
        self.widget.setLayout(self.vbox)

class Linechart():
    def __init__(self):
        self.mode = ""
        self.data = DEVICE_DATA()
        self.series = QLineSeries()
        

        self.series << QPointF(11,1) << QPointF(13,3)\
        << QPointF(17,6) << QPointF(18,3) << QPointF(20,20)
 
 
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Relative Moisture to Temperature Ratio")
        self.chart.setTheme(QChart.ChartThemeBlueCerulean)
        self.chart.createDefaultAxes()
 
        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)
        

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartview)
    def update_data(self):
        self.series = QLineSeries()
        self.data.get_data()
        for i in self.data.values:
            try:
                self.series.append(float(i[0]),float(i[1]))
            except:
                continue    

    def assign_chart(self,widget):
        self.widget.setLayout(self.vbox)

class Donutchart():
    def __init__(self):
        self.series = QPieSeries()
        self.series.setHoleSize(0.40)
 
        self.series.append("Protein 4,3%", 4.3)
 
        self.my_slice = self.series.append("Fat 15.6%", 15.6)
        self.my_slice.setExploded(True)
        self.my_slice.setLabelVisible(True)
 
        self.series.append("Other 30%", 30)
        self.series.append("Carbs 57%", 57)
 
 
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Dount Chart")
        self.chart.setTheme(QChart.ChartThemeBlueCerulean)
 
        self.chartview = QChartView(self.chart)
 
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartview)
    def assign_chart(self,widget):
        self.widget.setLayout(self.vbox)
class Scatterchart():
    def __init__(self):
        self.data = DEVICE_DATA()
        self.series = QScatterSeries()
        

        self.series << QPointF(11,1) << QPointF(13,3)\
        << QPointF(17,6) << QPointF(18,3) << QPointF(20,20)
 
 
        self.chart = QChart()
        self.chart.addSeries(self.series)
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Relative Moisture to Temperature Ratio")
        self.chart.setTheme(QChart.ChartThemeDark)
        self.chart.createDefaultAxes()
 
        self.chartview = QChartView(self.chart)
        #self.chartview.setRenderHint(QPainter.Antialiasing)
        

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.chartview)
    def update_data(self):
        self.series = QScatterSeries()
        self.data.get_data()
        for i in self.data.values:
            try:
                self.series.append(float(i[0]),float(i[1]))
            except:
                continue    
    def assign_chart(self,widget):
        self.widget.setLayout(self.vbox)
if __name__ == "__main__":           
    App = QApplication(sys.argv)
    #window = Window()
    #window.show()
    menu = Barchart()
    menu.assign_chart()
    sys.exit(App.exec())