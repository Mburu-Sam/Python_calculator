"""Step 1: Ask yhe user to enter a number and will use float since some numbers can contain decimals"""
"""Enter first number"""
number1 = float(input("Enter your first number: "))
"""Step 2 : """
"""Enter second  number"""
number2 = float(input("Enter the second number: "))


# Step 3: Time to do some math! 🧠 Let's compute the sum, difference, product, and quotient.
#Addition 
sum = number1 + number2

#Subtraction
differenceOfNumbers = number1 - number2

#Multiplication of two numbers
productOfNumbers = number1 * number2

# Divide the first number by the second
quotient = number1 / number2
if(number2 == 0):
    print("Can't divide bu zero")
else:
    print("Proceed")
#Modulas
remainder = number1 % number2

#Power

powerOfnum = number1 ** number2

# Step 4: Show the user what we got! 🥳 Time for the big reveal! 🎉
print("Result of your two numbers are:")
print(f"Sum: {sum}")
print(f"Difference: {differenceOfNumbers}")
print(f"Product: {productOfNumbers}")
print(F"Division: {quotient}")
print(f"The modulas is: {remainder}")
print(f"Power is: {powerOfnum}")
