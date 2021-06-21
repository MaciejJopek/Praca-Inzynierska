from app import app
from flask import request
import serial
from app.read_data import read_data_from_db
from flask import render_template
from mongodb_connection.db_operations import *
from mongodb_connection.connections import create_connection_to_database
@app.route('/', methods = ['POST','GET'])
def dashboard():
    if request.method == 'POST':
        led_port = get_led_port()
        ser = serial.Serial(led_port, 9600, timeout=10)
        if request.form['potwierdz'] == 'Włącz':
            ser.write(str.encode('1'))
        elif request.form['potwierdz'] == 'Wyłącz':
            ser.write(str.encode('0'))
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
    status_wszystkich_czujnikow = []
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
    ciecz = read_data_from_db("ciecz")
    status_temperatury = int(temperature.split()[0])
    status_wszystkich_czujnikow.append(status_temperatury)
    wartosc_temperatury = temperature.split()[1]
    status_wilgotnosci = int(wilgotnosc.split()[0])
    status_wszystkich_czujnikow.append(status_wilgotnosci)
    wartosc_wilgotnosci = wilgotnosc.split()[1]
    status_czystosc = int(czystosc.split()[0])
    status_wszystkich_czujnikow.append(status_czystosc)
    wartosc_czystosc = czystosc.split()[1]
    status_ciecz = int(ciecz.split()[0])
    status_wszystkich_czujnikow.append(status_ciecz)
    status = False
    if 0 in status_wszystkich_czujnikow or 1 in status_wszystkich_czujnikow:
        status = True
    else:
        status = False
    return render_template('index.html', temperature = wartosc_temperatury, status_temperatury = status_temperatury, status_wykresu_temoeratury = status_wykresu_temoeratury, x_temperature = x_temperature, y_temperature = y_temperature, x_wilgotnosc = x_wilgotnosc, y_wilgotnosc = y_wilgotnosc, status_wilgotnosci = status_wilgotnosci, watosc_wilgotnosci = wartosc_wilgotnosci, status_czystosc = status_czystosc, wartosc_czystosc = wartosc_czystosc, x_czystosc = x_czystosc, y_czystosc = y_czystosc, status_ciecz = status_ciecz, status = status  ) # moze te dane wrzycić do słownika



