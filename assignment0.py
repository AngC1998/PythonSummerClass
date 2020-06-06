def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

numOne = int(input("Enter in first number: "))
numTwo = int(input("Enter in second number: "))
floatOne = float(numOne)
floatTwo = float(numTwo)
result_addition = int(addition(floatOne, floatTwo))
result_subtraction = int(subtraction(floatOne, floatTwo))
result_multiply = int(multiply(floatOne, floatTwo))
result_divide = divide(floatOne, floatTwo)
print(str(numOne) + " + " + str(numTwo) + " = " + str(result_addition))
print(str(numOne) + " - " + str(numTwo) + " = " + str(result_subtraction))
print(str(numOne) + " * " + str(numTwo) + " = " + str(result_multiply))
print(str(numOne) + " / " + str(numTwo) + " = " + str(result_divide))