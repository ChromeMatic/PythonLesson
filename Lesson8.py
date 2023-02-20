# Function Parameters

# def greet(_name):
#     print(f"Hello comrade {_name}")
#     print(f"How are you doing comrade {_name}")
#
#
# name = input("Please enter your name: ")
# greet(name)

def greet_with(_name, _location):
    print(f"Hello comrade {_name}.")
    print(f"How is the weather in {_location}")


name = input("Please enter your name :")
location = input("Please enter your location")

greet_with(_location=str(location), _name=str(name))
