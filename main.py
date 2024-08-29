"""
PyPassword Generator

Author: Alan
Date: August 21st 2024

This script generates a random password based on the user's preferences for the number of letters, symbols, and numbers. 
The password is randomly shuffled to ensure security.
"""

import random

# Lists of characters to be used in the password
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
    'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
    'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# Get the number of letters, symbols, and numbers for the password from the user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Initialize an empty list to store the password characters
list_pass = []

# Generate the required number of letters and add them to the password list
for _ in range(nr_letters):
    list_pass.append(random.choice(letters))

# Generate the required number of symbols and add them to the password list
for _ in range(nr_symbols):
    list_pass.append(random.choice(symbols))

# Generate the required number of numbers and add them to the password list
for _ in range(nr_numbers):
    list_pass.append(random.choice(numbers))

# Randomly shuffle the characters in the password list to enhance security
random.shuffle(list_pass)

# Convert the list of characters into a string to form the final password
password = ''.join(list_pass)

# Display the generated password
print("Your generated password is:")
print(password)
