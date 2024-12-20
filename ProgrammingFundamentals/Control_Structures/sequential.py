# Sequential Control Structure

# Import the datetime module to work with the current year
import datetime

# Get current year using the now() method from datetime module
current_year = datetime.datetime.now().year

# Prompt the user to enter their name
name = input("Enter your name: ")

# Prompt the user to enter their age, converting it to an integer
age = int(input("Enter your age: "))

# Prompt the user to enter their city of residence
city = input("Enter your city of residence: ")

# Calculate the birth year by subtracting the age from the current year
birth_year = current_year - age

# Print a formatted message with all the gathered information
print(f"Hello, {name}! You are {age} years old and live in {city}. Based on your age, you were born in {birth_year}.")
