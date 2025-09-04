#Price of Nintendo Wii

wii_price = 299.99

#prompt user for how much $ they have

money = float(input("Enter the amount of money you have: $"))

#calculate how many they can afford
num_wiis_afforded = int(money // wii_price)

#calculate the remaining money needed for additional wiis

remaining_money = wii_price - (money % wii_price)

#display the results
print("You can afford", num_wiis_afforded, "Nintendo wiis")
print("You will need $", round(remaining_money,2), "more to afford an additional wii")