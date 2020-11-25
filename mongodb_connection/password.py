import pyzipper
from cryptography.fernet import Fernet
from mongodb_connection.connections import create_connection_to_database


def create_key():
    klucz = Fernet.generate_key()
    return klucz


def save_key_to_file(main_haslo):
    klucz = create_key()
    haslo_to_file = main_haslo 
    with pyzipper.AESZipFile('secret.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(haslo_to_file)
        zf.writestr('klucz.txt', klucz)


def get_key_from_file(main_haslo):
    haslo_to_file = main_haslo
    with pyzipper.AESZipFile('secret.zip') as zf:
        zf.setpassword(haslo_to_file)
        my_secrets = zf.read('klucz.txt')
        return(my_secrets)


def encrypt_password(paswd, main_haslo):
    klucz = get_key_from_file(main_haslo)
    password = paswd.encode('utf-8')
    fernet = Fernet(klucz)
    paswd = fernet.encrypt(password)
    return paswd


def decrypt_password(main_haslo):
    collection = create_connection_to_database()
    collection = collection.connect_to_db_password()
    password = collection.find_one({'haslo': {"$exists": True}})
    passwd = password['haslo']
    klucz = get_key_from_file(main_haslo)
    fernet= Fernet(klucz)
    decr = fernet.decrypt(passwd).decode()
    return decr

