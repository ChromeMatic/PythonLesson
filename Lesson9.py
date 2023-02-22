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

# Edit an element in dictionary
programming_dictionary["Bug"] = "A moth inside of your computer"

# Get elements form dictionary
for key in programming_dictionary:
    print(f" {key}: {programming_dictionary[key]}")

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a List in a dictionary
travel_log1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting a dictionary in a dictionary
travel_log2 = {
    "France": {
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
}

# Nesting a Dictionary in a list
travel_log_arr = [
    {
      "country": "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
    },
    {
      "country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 3
    }
]
