import random

sides = (1, 2, 3, 4, 5, 6)
count = 0
end = 100000
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
expected = end/6
numbers = []
while count < end:
  pick  = random.choice(sides)
  numbers.append(pick)
  count += 1
for num in numbers:
  if num == 1:
    one += 1
  elif num == 2:
    two += 1
  elif num == 3:
    three += 1
  elif num == 4:
    four += 1
  elif num == 5:
    five += 1
  elif num == 6:
    six += 1
  else:
    pass
print('Expected for each number: ' + str(expected))
print('1s were: ' + str(one))
print('2s were: ' + str(two))
print('3s were: ' + str(three))
print('4s were: ' + str(four))
print('5s were: ' + str(five))
print('6s were: ' + str(six))
