#  Lesson 6
#  Function and While loops and Code Block

# Functions in Python
def square_numbers(num):
    result = num ** 2
    return result


A_number = int(input("Please type a number: "))
final_result = 0

if type(A_number) != int:
    print("Please enter a number !")
else:
    final_result = square_numbers(A_number)
    print(f"Your answer is {final_result}")


def cube_number(num):
    result1 = num ** 3
    return result1

