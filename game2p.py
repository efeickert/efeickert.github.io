import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)
winner = 0
wait  = random.randint(1,5)
time.sleep(wait)

GPIO.output(7,GPIO.HIGH)
timestart = time.time()
while GPIO.input(38) == False and GPIO.input(40) == False: 
  if GPIO.input(38) == True:
    winner = 'Blue'
  if GPIO.input(40) == True:
    winner = 'Red'

time = timestart - time.time()
time = abs(time)
print(str(winner + " wins!"))
print("Your reaction time was " + "%.3f" % time + " seconds")
GPIO.output(7, GPIO.LOW)

GPIO.cleanup()




