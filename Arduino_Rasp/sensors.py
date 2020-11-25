import sys
import os
from Arduino_Rasp.main_loop import main_loop


def main(main_password):
    try:
        main_loop(main_password)
    except KeyboardInterrupt:
        print("Program został zakończony")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)