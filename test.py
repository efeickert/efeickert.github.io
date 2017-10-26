import time #Required for program to use time functions like sleep



pins = (7,11,13,15) #Creates list of GPIO pin numbers we want to interact with
n = 0

for i in range(4):
  print(pins[n])
  n += 1

print n
#time.sleep(3) #Wait for three seconds


