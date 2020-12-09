from app import app
from app.read_data import read_data_from_db
from flask import render_template
from mongodb_connection.db_operations import *
@app.route('/')
def dashboard():
    temperature_array = get_value_for_sensor_for_last_days(7, 'temperatura')
    status_wykresu_temoeratury = 0 if not temperature_array else 1
    wilgotnosc_array = get_value_for_sensor_for_last_days(7, 'wilgotnosc')
    czystosc_array = get_value_for_sensor_for_last_days(7, 'pyl')
    x_temperature = []
    y_temperature = []
    x_wilgotnosc = []
    y_wilgotnosc = []
    x_czystosc = []
    y_czystosc = []
    for value in temperature_array:
        for key, value in value.items():
            x_temperature.append(key)
            y_temperature.append(value)
    for value in wilgotnosc_array:
        for key, value in value.items():
            x_wilgotnosc.append(key)
            y_wilgotnosc.append(value)
    for value in czystosc_array:
        for key, value in value.items():
            x_czystosc.append(key)
            y_czystosc.append(value)
    temperature = read_data_from_db("temperatura")
    wilgotnosc = read_data_from_db("wilgotnosc")
    czystosc = read_data_from_db("pyl")
    status_temperatury = int(temperature.split()[0])
    wartosc_temperatury = temperature.split()[1]
    status_wilgotnosci = int(wilgotnosc.split()[0])
    wartosc_wilgotnosci = wilgotnosc.split()[1]
    status_czystosc = int(czystosc.split()[0])
    wartosc_czystosc = czystosc.split()[1]
    return render_template('index.html', temperature = wartosc_temperatury, status_temperatury = status_temperatury, status_wykresu_temoeratury = status_wykresu_temoeratury, x_temperature = x_temperature, y_temperature = y_temperature, x_wilgotnosc = x_wilgotnosc, y_wilgotnosc = y_wilgotnosc, status_wilgotnosci = status_wilgotnosci, watosc_wilgotnosci = wartosc_wilgotnosci, status_czystosc = status_czystosc, wartosc_czystosc = wartosc_czystosc, x_czystosc = x_czystosc, y_czystosc = y_czystosc  ) # moze te dane wrzycić do słownika



