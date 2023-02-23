# Calculator
# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operations = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}

num1 = int(input("What is the first number? : "))
num2 = int(input("What is the second number? : "))

for key in operations:
    print(f" {key}")
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
first_result = 0

if calculation_function == "add":
    first_result = add(num1, num2)
elif calculation_function == "subtract":
    first_result = subtract(num1, num2)
elif calculation_function == "multiply":
    first_result = multiply(num1, num2)
elif calculation_function == "divide":
    first_result = divide(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_result}")


