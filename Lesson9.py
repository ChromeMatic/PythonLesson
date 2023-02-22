# Dictionary

# Create a dictionary
programming_dictionary = {
    "Function": "A section or block code that is reusable.",
    "Bug": "An error in a program that prevents it from running"
}

# Adding a new element to dictionary
programming_dictionary["Loop"] = "The action of doing something repeatedly."

# Get elements form dictionary
# for key in programming_dictionary:
#     print(f" {key}: {programming_dictionary[key]}")

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)
programming_dictionary["Bug"] = "A moth inside of your computer"

# Get elements form dictionary
for key in programming_dictionary:
    print(f" {key}: {programming_dictionary[key]}")
