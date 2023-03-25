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
import bluetooth
import time
import os.path

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

    def find_sheet(self):
        #-------------------- Google Sheets Mode ----------------------------
        self.SERVICE_ACCOUNT_FILE = 'keys.json'
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.creds = None
        self.creds = service_account.Credentials.from_service_account_file(
                        self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.SAMPLE_SPREADSHEET_ID = '1FGpmOv6oRf8vKGUs_MtzeVuKZZ_qDUnGiIFHH58UF2A'
        self.values = ""
        self.mode = "sheet"
        

    def find_device(self):
        #-------------------- Bluetooth Mode -------------------------------
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

        nearby_devices = bluetooth.discover_devices(lookup_names=True)

        print("Found {} devices.".format(len(nearby_devices)))
        for addr, name in nearby_devices:
            print("  {} - {}".format(addr, name))

        if len(nearby_devices) == 1:
            msgBox.setText("Found 1 device, connect ?")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()
        elif len(nearby_devices) > 1:
            temp = ""
            for addr, name in nearby_devices:
                temp += "  {} - {}\n".format(addr, name)
            text, ok = QInputDialog.getText(None, "Choosing Device", temp+'Which one would you like to connect ?')
        else:
            msgBox.setText("Can't find any device nearby :((((")
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            returnValue = msgBox.exec()   
        


        


    def get_data(self):    
        try:
            self.service = build('sheets', 'v4', credentials=self.creds)
            # Call the Sheets API
            self.sheet = self.service.spreadsheets()
            self.result = self.sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range="velocity!A17:B30").execute()
            self.values = self.result.get('values', [])
            #print(result)
        except HttpError as err:
            print(err)
        
if __name__ == '__main__':
    tester = USER_DATA()
    check = DEVICE_DATA()
    check.get_data()