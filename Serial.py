import serial
import time

port = serial.Serial("COM7",9600)
data = int(input("Enter this"))

while port.isOpen():
    if(data == 1):
        port.write(1);
    else:
        port.write(0);