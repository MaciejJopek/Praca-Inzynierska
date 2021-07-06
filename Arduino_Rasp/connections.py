import serial

def connect_with_arduino(port):
    conn = serial.Serial(port, 9600)
    return conn

def disconnect_from_arduino(connection):
    connection.close()
