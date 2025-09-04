# The quadratic formula solves for the variable in any quadratic equation of the standard form ax² + bx + c = 0 (where a ≠ 0), 
# by using the equation: x = [-b ± √(b² - 4ac)] / 2a. You find the values of a, b, and c from your equation and then substitute 
# them into the formula to find the solutions for x

a = float(input("Enter the coefficient of a: "))
b = float(input("Enter the coefficient of b: "))
c = float(input("Enter the coefficient of c: "))

#promt the user enter the value of x

x = float(input("Enter the value of x: "))

#Evaluate the quadratic equation for the given coefficients and value of x

result = a * x**2 + b + x + c

print(f"The value of the quadratic equation for x = {x} is: {result}")