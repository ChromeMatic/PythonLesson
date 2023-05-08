# (OOP)
# Object-Oriented Programming In Python
# from turtle import Turtle, Screen
#
# Object = Turtle()
# Object.shape("turtle")
# Object.color("gold")
#
# Object.forward(100)
# Object.left(90)
# Object.forward(100)
# Object.left(90)
# Object.forward(100)
# Object.left(90)
# Object.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

names = ["Pikachu", "Squirtle", "Charmander"]
Types = ["Electric", "Water", "Fire"]

table = PrettyTable()

table.add_column("Pokemon Name", names)
table.add_column("Type", Types)

print(table)

