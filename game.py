import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(40, GPIO.IN)

wait  = random.randint(1,5)
time.sleep(wait)
print(wait)

GPIO.output(7,GPIO.HIGH)
timestart = time.time()
while GPIO.input(40) == False:
  pass
time = timestart - time.time()
time = abs(time)
print("%.3f" % time)
GPIO.output(7, GPIO.LOW)
#num = input('Enter a number: ')
#print ('Your number in binary is ' + num)

GPIO.cleanup()




