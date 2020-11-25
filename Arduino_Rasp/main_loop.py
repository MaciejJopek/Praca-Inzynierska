import serial
from Arduino_Rasp.connections import connect_with_arduino
from Arduino_Rasp.data_functions import data_operations
import threading
import time 

def connect_and_read(port, main_password):
    connection_status_port = False
    while True:
        if (connection_status_port == False):
            try:
                conn = connect_with_arduino(port)
                print("Nawiązano polaczenie z czujnikiem na porcie {}".format(port))
                connection_status_port = True
            except serial.serialutil.SerialException:
                connection_status_port = False    
        else:
            try:
                data_operations().read_data(conn, main_password)
            except serial.serialutil.SerialException:
                connection_status_port = False


def main_loop(main_password):
    test = threading.Thread(target=connect_and_read, args=("COM3", main_password))
    test.start()
    testowo = threading.Thread(target=connect_and_read,  args=("COM4", main_password))
    testowo.start()



       
            
            
        