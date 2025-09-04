#Calaculate simple interest by gathering three things (principle, number of years, rate of interest) from user input.

print("To calculate your simple interest please enter the following information")

#get user input
user_p = input("Enter Principal (original amount of money borrowed or invested): ")
user_n = input("Enter the number of years: ")
user_r = input("Enter the interest rate as percentage: ")

#Convert user input to integers (Add float() to ensure decimals are also converted to integer)
p = int(float(user_p))
n = int(float(user_n))
r = int(float(user_r))

#Calculate the simple interest of p,n,r (multiply p,n,r, and then divide by 100)

simple_interest = (p * n * r)/100

#print simple interest
print("Your Simple Interest is: ", simple_interest)


