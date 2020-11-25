import serial

def connect_with_arduino(port):
    conn = serial.Serial(port, 9600)
    return conn