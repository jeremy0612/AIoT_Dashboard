from __future__ import print_function
from cgi import test
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from PyQt5.QtWidgets import QMessageBox, QApplication, QTableWidget, QTableWidgetItem, QInputDialog
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import time
import os.path

import serial
import serial.tools.list_ports

class DATA():
    def __init__(self):
        self.SERVICE_ACCOUNT_FILE = 'keys.json'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                        self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        # If modifying these scopes, delete the file token.json.
        # The ID and range of a sample spreadsheet.
        #self.SAMPLE_SPREADSHEET_ID = '1FGpmOv6oRf8vKGUs_MtzeVuKZZ_qDUnGiIFHH58UF2A'
        self.SAMPLE_SPREADSHEET_ID = '1TRFv5LPwcWFbFCeFURMToUzoLNVPfpUChfTI0shw7B4'     
    def Get_sheet_inform(self):
        try:
            self.service = build('sheets', 'v4', credentials=self.creds)
            # Call the Sheets API
            self.sheet = self.service.spreadsheets()
            self.result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range="Log_in_in4!A1:B2").execute()
            self.values = self.result.get('values', [])
            #print(result)
        except HttpError as err:
            print(err)

class USER_DATA(DATA):
    def __init__(self):
        super().__init__()
        self.SERVICE_ACCOUNT_FILE = 'keys.json'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                        self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.SAMPLE_SPREADSHEET_ID = '1TRFv5LPwcWFbFCeFURMToUzoLNVPfpUChfTI0shw7B4'
        try:
            self.service = build('sheets', 'v4', credentials=self.creds)
            # Call the Sheets API
            self.sheet = self.service.spreadsheets()
            self.result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range="Log_in_in4!A1:B2").execute()
            self.values = self.result.get('values', [])
            #print(result)
        except HttpError as err:
            print(err)
class DEVICE_DATA(DATA):
    def __init__(self):
        super().__init__()
        self.mode = ""
        self.values = []
        self.x = 1

    def find_sheet(self):
        #-------------------- Google Sheets Mode ----------------------------
        if self.mode != "sheet":
            self.values = []
            self.mode = "sheet"
        self.SERVICE_ACCOUNT_FILE = 'keys.json'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                        self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.SAMPLE_SPREADSHEET_ID = '1FGpmOv6oRf8vKGUs_MtzeVuKZZ_qDUnGiIFHH58UF2A'
        
        

    def find_device(self):
        #-------------------- Bluetooth Mode -------------------------------
        if self.mode != "bluetooth":
            self.values = []
            self.mode = "bluetooth"
        # create a message box object
        msgBox = QMessageBox()
        # set the window title and text message
        msgBox.setWindowTitle("Loading!")
        msgBox.setText("Finding Device, please wait !!!")
        # set the icon and buttons
        msgBox.setIcon(QMessageBox.Information)
        # execute the message box
        #msgBox.setStandardButtons(QMessageBox.NoButton)
        #msgBox.setWindowFlags(msgBox.windowFlags() | QtCore.Qt.FramelessWindowHint)
        returnValue = msgBox.exec()
        # get a list of all the available serial ports
        ports = serial.tools.list_ports.comports()

        print("Found {} devices.".format(len(ports)))
        # print the description and hardware ID of each port
        for port in ports:
            print("Description: ", port.description, ", Hardware ID: ", port.hwid)

        device_port = None

        if len(ports) == 1:
            msgBox.setText("Found 1 device, connect ?")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
            if returnValue == QMessageBox.Ok:
                device_port = str(ports[0].description.split()[-1]).replace(")( ",'')
            elif returnValue == QMessageBox.Cancel:
                return
        elif len(ports) > 1:
            temp = ""
            for port in ports:
                temp += "Description: {} - Hardware ID: {}\n".format(port.description, port.hwid)
            text, ok = QInputDialog.getText(None, "Choosing Device", temp+'Which one would you like to connect ?')
            try:
                device_port = str(ports[int(text)].description.split()[-1]).replace("(",'').replace(")",'')
            except:
                return
            print(device_port)
        else:
            msgBox.setText("Can't find any device :((((")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec() 
            return
        try:
            self.device = serial.Serial(device_port, 9600)
        except:
            return 

    def get_data(self):  
        if self.mode == "sheet":  
            try:
                #self.values = []
                self.service = build('sheets', 'v4', credentials=self.creds)
                # Call the Sheets API
                self.sheet = self.service.spreadsheets()
                self.result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                            range="velocity!A17:B30").execute()
                self.values = self.result.get('values', [])

            except HttpError as err:
                print(err)
        else:
            try:
                #while True:
                #data = self.device.read_all()
                #print(type(data),size(data))
                data = str(self.device.read_all()).split("\\r\\n")[:-1]
                #print(data)
                data[0].rstrip("b'")
                print(data)
                print("++@",self.values,self.values[:-1])
                #if len(self.values >= 14):
                 #   self.values = self.values[:-1]
                #self.values = []
                for i in data:
                    try:
                        self.values.append([float(i),self.x])
                        self.x += 1
                    except:
                        continue                
                if self.device.in_waiting > 0:  # check if there is any data in the buffer
                    data = self.device.readline().decode('utf-8').rstrip()  # read the data from the buffer and decode it
                    self.values += data
                    print(data,type(data))  # print the received data to the console

            except:
                msgBox.setText("Device invalid !!!")
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                returnValue = msgBox.exec() 
    def send_command(self,command):
        self.device.write(b'{}\n'.format(command))
        pass

            
if __name__ == '__main__':
    tester = USER_DATA()
    check = DEVICE_DATA()
    check.get_data()