# -*- coding: utf-8 -*-
import time
import datetime
import threading

def oblicz(x):
    time.sleep(x)
    return x * x

# dodajemy stempelek czasowy do komunikatu

def log(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print "%s %s" % (now, message)

# kazde zadanie obliczweniowe uruchomione jest w osobnym watku

class WatekOblicz(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value
    def run(self):
        result = oblicz(self.value)
        log("%s -> %s" % (self.value, result))

def main():
    log("uruchamiam watek glowny")
    WatekOblicz(3).start()
    WatekOblicz(2.5).start()
    WatekOblicz(1).start()
    log("koniec watku głownego")

if __name__ == "__main__":
    main()