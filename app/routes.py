from app import app
from app.read_data import read_data_from_db

@app.route('/')
def dashboard():
    temperature = read_data_from_db("temperatura", "temperatury")
    wilgotnosc  = read_data_from_db("wilgotnosc", "wilgotnosci")
    return "{} {}".format(str(temperature),str(wilgotnosc))


