import math
def factorial(n):

#Compute the factorial of an integer n.

    if n == 0: 
        return 1
    else: 
        return n * factorial(n-1)
    
#Promp the user for enter an integer
num = int(input("Enter an integer: "))

#Check if the number is negative
if num < 0:
    print("Factorial is not defined for negative numbers")
else: 
    #computing and printing the factorial value
    result = factorial(num)
    print (f"The factorial of {num} is: {result}")
    x = 30
    if x <= 15:
        y = x + 15
    elif x <= 30:
        y = x + 30
    else:
        y = math.sin(x)
    print("The value of y is", y)
