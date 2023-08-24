from var import *
from ultrasonic import *
import RPi.GPIO as GPIO
import time

def init():
    # GPIO Modus (BOARD / BCM)
    GPIO.setmode(GPIO.BCM)

    # Richtung der GPIO-Pins festlegen (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)


def destroy():
    GPIO.cleanup()

def measurement():
    try:
        while True:
            SONIC_LEFT.getDistance()
            #SONIC_RIGHT.getDistance()
            #SONIC_BACK.getDistance()
            #SONIC_FRONT.getDistance()
            #print("Distanz Hinten:", SONIC_BACK.distance)
            #print("Distanz Vorne:", SONIC_FRONT.distance)
            #print("Distanz Rechts:", SONIC_RIGHT.distance)
            print("Distanz Links:", SONIC_LEFT.distance)

            time.sleep(1)

        # Beim Abbruch durch STRG+C resetten
    except KeyboardInterrupt:
        print("Messung vom User gestoppt")
        destroy()


SONIC_LEFT = ultraSonic(GPIO_ECHO_SENSOR_LEFT)
#SONIC_BACK = ultraSonic(GPIO_ECHO_SENSOR_BACK)
#SONIC_FRONT = ultraSonic(GPIO_ECHO_SENSOR_FRONT)
#SONIC_RIGHT = ultraSonic(GPIO_ECHO_SENSOR_RIGHT)
