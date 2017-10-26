import RPi.GPIO as GPIO #Required for program to interact with GPIO pins
import time #Required for program to use time functions like sleep

GPIO.setmode(GPIO.BOARD) #Sets which pin numbering to use: board vs bcm
pins = (7,11,13,15) #Creates list of GPIO pin numbers we want to interact with
GPIO.setup(pins, GPIO.OUT) #Sets all GPIO pins in "pins" list as outputs

p = 0

GPIO.output(pin[p], GPIO.HIGH)
time.sleep(0.1)
GPIO.output(pin[p], GPIO.LOW)

GPIO.output(11, GPIO.HIGH)
GPIO.output(13, GPIO.HIGH)
GPIO.output(15, GPIO.HIGH)

#time.sleep(3) #Wait for three seconds

GPIO.cleanup() #Returns all GPIO pins back to their default state (input) so they can be used by another program after this program terminates




