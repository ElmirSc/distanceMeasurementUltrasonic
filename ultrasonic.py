from var import *
from ultrasonic import *
import RPi.GPIO as GPIO
import time

class ultraSonic():
    def __init__(self,pinNumber):
        self.distance = 0
        self.pin = pinNumber
        GPIO.setup(self.pin, GPIO.IN)

    def getDistance(self):
        # setze Trigger auf HIGH
        GPIO.output(GPIO_TRIGGER, True)

        # setze Trigger nach 0.01ms aus LOW
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartZeit = time.time()
        StopZeit = time.time()

        # speichere Startzeit
        while GPIO.input(self.pin) == 0:
            StartZeit = time.time()

        # speichere Ankunftszeit
        while GPIO.input(self.pin) == 1:
            StopZeit = time.time()

        # Zeit Differenz zwischen Start und Ankunft
        TimeElapsed = StopZeit - StartZeit
        # mit der Schallgeschwindigkeit (34300 cm/s) multiplizieren
        # und durch 2 teilen, da hin und zurueck
        self.distance = (TimeElapsed * 34300) / 2