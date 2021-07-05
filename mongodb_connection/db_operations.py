from mongodb_connection.connections import create_connection_to_database
from mongodb_connection.password import *
from datetime import datetime, timedelta
import getpass


def get_last_n_days(days, czujnik):
    czas = (datetime.now() - timedelta(days))
    czas = czas.strftime("%Y-%m-%d %H:%M:%S")
    client = create_connection_to_database()
    db = client.connect_to_db()
    records = db.find({'data' : {"$gte": czas }, 'czujnik' : czujnik}, {'_id' : 0})
    return records


def get_value_for_sensor_for_last_days(days, czujnik):
    array = []
    records = get_last_n_days(days, czujnik)
    for x in records:
        dic = {x['data'] : x['wartosc']}
        array.append(dict(dic))
    return array
    

def check_password():
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    password  = collection.find()
    return False if password == None else True


def check_main_password():
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    password = collection.find({"haslo_glowne": {"$exists": True}}).limit(1)
    return False if password.count() == 0 else True


def settings():
    return check_main_password()


def set_account(main_haslo):
    print ("Brak ustawionego konta e-mail. Prosze utawić konto porzed pierwszym użyciem programu")
    email = input("Podaj email: ")
    paswd = getpass.getpass('Podaj haslo do konta email:')
    save_key_to_file(main_haslo)
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    collection.insert_one({'email' : email, 'haslo' : encrypt_password(paswd, main_haslo)})
    print ("Konto email zostało ustawione")


def get_led_port():
    client = create_connection_to_database()
    db = client.connect_to_db()
    records = db.find({'czujnik' : 'led'}).sort('data', -1)
    client.disconnect_from_db()
    list_of_led_ports = [x for x in records]
    return list_of_led_ports[0]['wartosc'] if len(list_of_led_ports) != 0 else 'None'