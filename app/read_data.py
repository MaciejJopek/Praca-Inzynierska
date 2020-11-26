from pymongo import MongoClient
from datetime import datetime, timedelta

def read_data_from_db(czujnik):
    clinet = MongoClient()
    db = clinet.pomiary
    collection = db.czujniki_dane
    last_data = collection.find().sort("czujnik")
    tab=[]
    for x in last_data:
        if x["czujnik"] == czujnik:
            tab.append(x)
    if tab:
        last_record = tab[-1]["data"] 
        czas = datetime.now()
        czas = czas.strftime("%Y-%m-%d %H:%M:%S")
        d1 = datetime.strptime(last_record, '%Y-%m-%d %H:%M:%S')
        d2 =  datetime.strptime(czas, '%Y-%m-%d %H:%M:%S')
        diff = (d2 - d1).total_seconds()
        if (diff > 10):
            last_record = tab[-1]["wartosc"]
            return "0 {}".format(last_record)
        else:
            last_record = tab[-1]["wartosc"] 
            return "1 {}".format(last_record)
    else:
        return 0



