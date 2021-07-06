
import datetime
from Arduino_Rasp.connections import connect_with_arduino
from mongodb_connection.connections import create_connection_to_database
from Arduino_Rasp.mail_sender import send_email
import threading

class data_operations():

    def read_data(self, conn, main_password, port):
        data = conn.readline()[:-2]             
        data = data.decode('utf-8')
        if "Wilgotnosc" in data:
            self.temp_hum_data_processing(data)
        if "Gaz" in data:
            self.gaz_data_processing(data)
        if "zalanie" in data:
            self.czujnik_alarmowy(data, main_password)
        if "1_zal" in data:
            self.liquid_level_data_processing(data)
        if "1_led" in data:
            self.led(data, port)
        return data

    def czujnik_alarmowy(self, data, main_password):
        if "zalanie" in data:
            send_email(main_password)

    def temp_hum_data_processing(self, data):
        wilgotnosc = data[10:12] 
        temperatura = data [23:25]
        pyl = data[28:]
        self.add_wilgotnosc_and_temp_to_db(wilgotnosc, temperatura, pyl)


    def add_wilgotnosc_and_temp_to_db(self, wilgotnosc, temperatura, pyl):
        collection = create_connection_to_database()
        collection = collection.connect_to_db()
        czas = datetime.datetime.now()
        czas = czas.strftime("%Y-%m-%d %H:%M:%S")
        dane_model_temperatura = {
            'data': czas,
            'wartosc': int(temperatura),
            'czujnik': 'temperatura'
        }
        dane_model_wilgotnosc = {
            'data': czas,
            'wartosc': int(wilgotnosc),
            'czujnik': 'wilgotnosc'
        }
        dane_model_pyl = {
            'data': czas,
            'wartosc': float(pyl),
            'czujnik': 'pyl'
        }
        result = collection.insert_many([dane_model_temperatura, dane_model_wilgotnosc, dane_model_pyl])

    def liquid_level_data_processing(self, data):
        data = data[0]
        collection = create_connection_to_database()
        collection = collection.connect_to_db()
        czas = datetime.datetime.now()
        czas = czas.strftime("%Y-%m-%d %H:%M:%S")
        dane_model_poziom_cieczy = {
            'data': czas,
            'wartosc': int(data),
            'czujnik': 'ciecz'
        }
        result = collection.insert_many([dane_model_poziom_cieczy])

    def gaz_data_processing(self, data):
        pass

    def led(self,data, port):
        collection = create_connection_to_database()
        collection = collection.connect_to_db()
        czas = datetime.datetime.now()
        czas = czas.strftime("%Y-%m-%d %H:%M:%S")
        dane_model_led = {
            'data': czas,
            'wartosc': str(port),
            'czujnik': 'led'
        }
        result = collection.insert_many([dane_model_led])




