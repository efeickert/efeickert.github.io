import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
pins = (7, 11, 13, 15)
GPIO.setup(pins, GPIO.OUT)

pick  = random.choice(pins)
print(pick)
GPIO.output(pick, GPIO.HIGH)
time.sleep(3)
GPIO.output(pick, GPIO.LOW)
GPIO.cleanup()




