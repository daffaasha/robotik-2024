import BlynkLib
from time import sleep
import RPi.GPIO as GPIO
import time
import random

BLYNK_AUTH = 'CARI AUTH PADA AKUN BLYNK'

#LED Button Buzzer
# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)
GPIO.setmode(GPIO.BCM)

#setup led
GPIO.setup(18, GPIO.OUT)


print("Blynk Connected!")

@blynk.on("V1")
def v1_handler(value):
    print(value[0])
    values= int(value[0])
    GPIO.output(18, values)
    #menerima data dari v1

while True:
    blynk.run()
