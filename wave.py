import time
"""
GPIO config



"""
counter = 0
end = 3
counter2 = 0
end2 = len(pins)
pins = [1,2,3,4]

while counter < end
  counter2 = 0
  while counter2 < end2
    #light up pin counter2 of "pins"
    time.sleep(0.2)
    #Turn off LED
    counter2 += 1
  while counter2 > 0
    #light up pin counter2 of "pins"
    time.sleep(0.2)
    #Turn off LED 
    counter2 -= 1
  counter += 1
GPIO.cleanup()
