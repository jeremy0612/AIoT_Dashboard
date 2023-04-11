import serial
import serial.tools.list_ports

# get a list of all the available serial ports
ports = serial.tools.list_ports.comports()

# print the description and hardware ID of each port
for port in ports:
    print("Description: ", port.description, ", Hardware ID: ", port.hwid)

ser = serial.Serial('COM9', 9600)  # open the serial port at 9600 baud rate

while True:
    if ser.in_waiting > 0:  # check if there is any data in the buffer
        print("got")
        data = ser.readline().decode('utf-8').rstrip()  # read the data from the buffer and decode it
        print(data,type(data))  # print the received data to the console
