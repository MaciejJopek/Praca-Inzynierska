from app import app
import threading
from Arduino_Rasp.sensors import main
from mongodb_connection.db_operations import set_account, check_password, settings
from mongodb_connection.password_operation import hashowanie_hasla, add_password_to_mongo_db, dehashowanie_hasla

def run_app(main_password):
    if __name__ == '__main__':
        x = threading.Thread(target=main,  args=(main_password,), daemon=True)
        x.start()
        app.run(host="192.168.1.8")

if settings() == False:
    print("Aplikacja nie została skonfigurowana")
    haslo = input("podaj haslo: ")
    haslo_bite = hashowanie_hasla(haslo) #to jest dlugi string
    add_password_to_mongo_db(haslo_bite)
    set_account(haslo.encode('utf-8'))
    # sprobujmy wyslać maila w celu walidacji prawidlowego maila
    run_app(haslo.encode('utf-8'))
else:
    try:
        haslo = input("Proszę podać hasło do aplikacji: ")
        dehashowanie_hasla(haslo)
        #ask for change crudencials if nie to run else update db  and try to send mail
        run_app(haslo.encode('utf-8'))
    except AssertionError:
        print("Podane błedne hasło")


    