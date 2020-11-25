from connections import connect_with_arduino
import serial 
from data_functions import data_operations
conn = connect_with_arduino("COM4")

while True:
    date = data_operations()
    data = date.read_data(conn)
