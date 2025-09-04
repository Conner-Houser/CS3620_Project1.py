
#Write Python code to open a file named demo.txt and write some random data into it.
with open ("demo.txt", "w") as input_file:
    input_file.write("Hummingbirds: are the only birds capable of flying backward.")


#Open the file, read the contents, and display them as output
with open("demo.txt", 'r') as input_file:
    print(input_file.read())