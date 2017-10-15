import RPi.GPIO as GPIO
import time
# build all functions
def blink(pin):
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(0.02)
        GPIO.output(pin,GPIO.LOW)
        return
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
# blink GPIO17 100 times
for i in range(0,100):
	blink(7)
	blink(11)
	blink(13)
	blink(15)
GPIO.cleanup()
