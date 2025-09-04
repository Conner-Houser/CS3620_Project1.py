#Create a list of your favorites food items, list should have a minimum of 5 elements

#List of favorite foods
favorite_foods = ["Sushi", "Pasta", "BBQ", "Ramen", "Burrito"]

#list out the 3rd element in the list
print("3rd element in list: ", favorite_foods[2])

#add additional items to the current list 
favorite_foods.append("Hamburger")
favorite_foods.append("Pizza")

#use a loop to display the list
print("Display all items in list:")
for item in favorite_foods:
    print(item)

#insert an element named tacos at the 3rd index of the list and print out the "odd" elements in the list by using a loop
favorite_foods.insert(2, "Tacos")
print(favorite_foods)

print('Display "odd" elements: ')
#Use len to identify number of items in list 
for i in range(len(favorite_foods)):
    if i % 2 != 0: #if number in list % 2 doesn't equal 0 it is a odd number and we can print that item
        print(favorite_foods[i])



