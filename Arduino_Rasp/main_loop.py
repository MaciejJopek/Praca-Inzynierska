import serial
from Arduino_Rasp.connections import connect_with_arduino, disconnect_from_arduino
from Arduino_Rasp.data_functions import data_operations
import threading
import time 

def connect_and_read(port, main_password):
    connection_status_port = False
    connection_status_led = False
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
                data = data_operations().read_data(conn, main_password, port)
                if data == "1_led":
                    connection_status_led = True
            except serial.serialutil.SerialException:
                connection_status_port = False
        if connection_status_led == True:
            disconnect_from_arduino(conn)
            break


def main_loop(main_password):
    test = threading.Thread(target=connect_and_read, args=("COM3", main_password))
    test.start()
    testowo = threading.Thread(target=connect_and_read,  args=("COM4", main_password))
    testowo.start()
    testowo2 = threading.Thread(target=connect_and_read,  args=("COM5", main_password))
    testowo2.start()


       
            
            
        