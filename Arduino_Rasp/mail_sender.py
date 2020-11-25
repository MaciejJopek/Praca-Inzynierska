import smtplib, ssl
from mongodb_connection.password import decrypt_password
# haslo = "pracainz94"

wiadomosc = """Subject: Alarm

Wykryto zalanie pomieszczenia"""


def send_email(main_password):
    haslo_do_maila = decrypt_password(main_password)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login("labolatorium.mail@gmail.com", haslo_do_maila)
        server.sendmail("labolatorium.mail@gmail.com", "labolatorium.mail@gmail.com", wiadomosc)