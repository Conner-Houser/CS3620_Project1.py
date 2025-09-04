# Using break statement
print("Using break statement:")
for i in range(1, 6):
    if i == 4:
        print("Breaking the loop at", i)
        break
    print("Current value is", i)


# Using continue statement
print("\nUsing continue statement:")
for i in range(1, 6):
    if i == 3:
        print("Skipping", i)
        continue
    print("Current value is", i)


# Using pass statement
print("\nUsing pass statement:")
for i in range(1, 6):
    if i == 2:
        print("Encountered", i, "but doing nothing")
        pass
    else:
        print("Current value is", i)