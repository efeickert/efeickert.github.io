import RPi.GPIO as GPIO #Required for program to interact with GPIO pins
import time #Required for program to use time functions like sleep

GPIO.setmode(GPIO.BOARD) #Sets which pin numbering to use: board vs bcm
pins = (7,11,13,15) #Creates list of GPIO pin numbers we want to interact with
GPIO.setup(pins, GPIO.OUT) #Sets all GPIO pins in "pins" list as outputs
  
num = input('Enter number: ') #Ask user for number
num = bin(num) #Convert number to binary
num = num[2:] #Strip 0b identifier that Python adds during binary conversion
num = num.zfill(4) #Print four digit number adding leading zeros if needed
print ('Your number in binary is ' + num) #Prints your number in binary

if num[0] == '1': #If the first digit is a 1 then
  GPIO.output(7, GPIO.HIGH) #make pin 7 high, turning on LED1
if num[1] == '1': #If the second digit is a 1 then
  GPIO.output(11, GPIO.HIGH) #make pin 11 high, turning on LED2
if num[2] == '1': #If the third digit is a 1 then
  GPIO.output(13, GPIO.HIGH) #make pin 13 high, turning on LED3
if num[3] == '1': #If the fourth digit is a 1 then
  GPIO.output(15, GPIO.HIGH) #make pin 15 high, turning on LED4

time.sleep(3) #Wait for three seconds

GPIO.cleanup() #Returns all GPIO pins back to their default state (input) so they can be used by another program after this program terminates




