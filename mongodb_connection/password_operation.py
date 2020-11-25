import hashlib, os
from mongodb_connection.connections import create_connection_to_database


def hashowanie_hasla(haslo):
    random = os.urandom(32)
    zahashowane_haslo = hashlib.pbkdf2_hmac("sha256", haslo.encode('utf-8'), random, 100000)
    calosc = zahashowane_haslo+random
    return zahashowane_haslo + random


def add_password_to_mongo_db(haslo):
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    collection.insert_one({'haslo_glowne' : haslo})


def dehashowanie_hasla(haslo):
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    password = collection.find_one({'haslo_glowne': {"$exists": True}})
    passwd = password['haslo_glowne']
    random = passwd[32:]
    obecne =  passwd[:32]
    zahashowane_haslo = hashlib.pbkdf2_hmac("sha256", haslo.encode('utf-8'), random, 100000)
    assert zahashowane_haslo == obecne
