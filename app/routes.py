from app import app
from app.read_data import read_data_from_db
from flask import render_template
from mongodb_connection.db_operations import *
@app.route('/')
def dashboard():
    temperature_array = get_value_for_sensor_for_last_days(7, 'temperatura')
    x_temperature = []
    y_temperature = []
    for value in temperature_array:
        for key, value in value.items():
            x_temperature.append(key)
            y_temperature.append(value)
    temperature = read_data_from_db("temperatura")
    status_temperatury = int(temperature.split()[0])
    wartosc_temperatury = temperature.split()[1]
    return render_template('index.html', temperature = wartosc_temperatury, status_temperatury = status_temperatury )


