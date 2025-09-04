def bottles_of_beer(num_bottles):
    """
    Print the lyrics of the "99 Bottles of Beer" song.
    """
    for i in range(num_bottles, 0, -1):
        if i == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.")
        else:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i-1} bottles of beer on the wall.")
        print() # Print an empty line for better readability

    # Print the last verse
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

# Call the function to print the lyrics with 99 bottles
bottles_of_beer(99)
sum = 0
for i in range(1, 11):
    sum = sum + (i * i)
print ("sum of first 10 squares is", sum)
