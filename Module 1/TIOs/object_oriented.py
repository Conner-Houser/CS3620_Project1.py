# object_oriented.py

#Create computer superclass
class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None

    def getspecs(self):
        #Get computer specifications from the user
        self.cpu = input("Enter CPU: ")
        self.ram = input("Enter RAM size (GB): ")
        self.storage = input("Enter Storage size (GB): ")

    def displayspecs(self):
        #Display the computer specifications
        print("\n--- Computer Specifications ---")
        print(f"CPU: {self.cpu}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")

# Create Dekstop subclass
class Desktop(Computer):
    def __init__(self):
        #inherit attributes form computer superclass
        super().__init__()
        self.form_factor = None  # Unique property for Desktop

    # Overriding the parent's getspecs method
    def getspecs(self):
        super().getspecs()  # Call the parent's getspecs
        self.form_factor = input("Enter Desktop Form Factor (Tower, Mini, etc...): ")
        print("Desktop specifications collected successfully!")

    #Overriding displayspecs for Desktop
    def displayspecs(self):
        super().displayspecs() # Call parent method displayspecs
        print(f"Form Factor: {self.form_factor}")

#Create Laptop subclass
class Laptop(Computer):
    def __init__(self):
        #inherit attributes form computer superclass
        super().__init__()
        self.weight = None  # Unique property for Laptop

    #Overriding parent getspecs method
    def getspecs(self):
        super().getspecs() #Call parent method getspecs
        self.weight = input("Enter Laptop Weight (lbs): ")

    #Overriding dispalyspecs for Laptop
    def displayspecs(self):
        super().displayspecs()#Call parent method displayspecs
        print(f"Weight: {self.weight} lbs")


# Demonstration Code 
if __name__ == "__main__":
    print("Choose device type to enter specifications:")
    print("1. Desktop")
    print("2. Laptop")
    choice = input("Enter choice (1 or 2): ")

    # Object based choice for user to pick
    if choice == "1":
        device = Desktop()
    else:
        device = Laptop()

    # Call methods to collect and display specs
    device.getspecs()
    device.displayspecs()














