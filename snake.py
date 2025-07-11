print("Welcome to the Interactive Personal Data Collector!")
print("This program will collect and display your personal information.\n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
favorite_number = int(input("Please enter your favourite number: "))

current_year = 2025
birth_year = current_year - age

print("\nThank you! Here is the information we collected:")
print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(f"Favourite Number: {favorite_number} (Type: {type(favorite_number)}, Memory Address: {id(favorite_number)})")

print(f"\nYour birth year is approximately: {birth_year} (based on your age of {age})")

rounded_height = int(height)
print(f"\nType Conversion Example: Your height ({height}) was converted to an integer: {rounded_height}")
print(f"Rounded Height (Type: {type(rounded_height)}, Memory Address: {id(rounded_height)})")

print("\nThank you for using the Personal Data Collector. Goodbye!")