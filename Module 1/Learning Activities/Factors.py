def factors_count(n):
    # Display and count the factors of a number n.

    factors = [] #Initialize an empty list to store factors
    count = 0 #Initialize the count of the factors

    #Iterate from 1 to n

    for i in range (1, n + 1):
        if n % i == 0:  #Check if i is a factor of n
            factors.append(i) #add i to the list of factors
            count += i       # Increment Count
    
    #Display the factors
    print("FActors of", n, "are:", factors)
    print("Total number of facators:", count)

#prompt the user to enter a number
55
num = int(input("Enter a number: "))

#call function to display and count factors
factors_count(num)
