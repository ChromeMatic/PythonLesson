# Loops in python

# Useful python functions: range, sum

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print("\n "+fruit)
#
# for number in range(1, 101):
#     if number % 3 == 0 & number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

# Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""
random_letter = ""

for letter in range(1, nr_letters + 1):
    password += random.choice(letters)

for number in range(1, nr_numbers + 1):
    password += random.choice(numbers)

for symbol in range(1, nr_symbols + 1):
    password += random.choice(symbols)

print(password)

sizeOfPassword = list(password)
random.shuffle(sizeOfPassword)

Final_password = ''.join(sizeOfPassword)
print(Final_password)
