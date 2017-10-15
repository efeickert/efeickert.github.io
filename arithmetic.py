# This line imports the math for the program
import math

# The next 2 lines get 2 numbers from you, and store them in variables firstNumber and secondNumber.
firstNumber = input("Enter the first number: ")
secondNumber = input("Enter the second number: ")
compute = 0

# The next line stores the function that it will play between the first and second numbers such as adding, multiplying, etc. See, this can help you with your math homework!
function = raw_input("Enter a  math function such as adding, type 'help' to list all functions, or type 'exit' to exit: ")                

# Calm down, the lines that follow are not hard to understand! These lines figure out if you wanted to add the numbers, etc, and then compute what you want and return the result.
if function == "add":  
#This line adds the numbers
  compute = firstNumber + secondNumber
elif function =="subtract":
#This line subtracts the numbers
  compute = firstNumber - secondNumber
elif function == "multiply":
#This line multipies the numbers
  compute = firstNumber * secondNumber
elif function == "divide":
#This line  divides the numbers
  compute = firstNumber / secondNumber
elif function == "exponent":
#This line takes the first number and uses the second for the exponent
  compute = firstNumber ** secondNumber
elif function == "help":
#This line displays all of the functions
  print("add, subtract, multiply, divide, exponent")
else:
  print("Your function is invalid.")
print("Your answer is " + str(compute))
