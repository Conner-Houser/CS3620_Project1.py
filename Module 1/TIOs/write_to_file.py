#Create product dictionary
product_dictionary = {
    "computer": "$343.00",
    "printer": "$55.55",
    "phone": "829.99",
    "xbox": "549.99",
    "PS5": "499.99"
    }

#open demo.txt file and append items
with open ("demo.txt", "a") as file:
    for product, price in product_dictionary.items():

        #create printed format for each item
        output_line = (f"The {product} sells for ${price}\n")

        #write each line into file
        file.write(output_line)

#confirmation that data has been appended
print("Data has been appended to demo.txt")