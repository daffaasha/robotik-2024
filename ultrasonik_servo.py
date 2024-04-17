# Import libraries
import RPi.GPIO as GPIO
import time

# Set GPIO numbering mode
GPIO.setmode(GPIO.BCM)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(27,GPIO.OUT)
servo1 = GPIO.PWM(27,50) # Note 11 is pin, 50 = 50Hz pulse

#set GPIO Pins
GPIO_TRIGGER = 4
GPIO_ECHO = 17
# GPIO_BUZZER = 23

# Define variable duty
duty = 2

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
# GPIO.setup(GPIO_BUZZER, GPIO.OUT)

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance

while True:
    dist = int(distance())
    print (f"Measured Distance = {dist} cm")
    time.sleep(2)

    if dist > 50:
        servo1.ChangeDutyCycle(7)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(0.5)
    else:
        servo1.ChangeDutyCycle(2)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(0.5)


    # #Clean things up at the end
    # servo1.stop()
    # GPIO.cleanup()
