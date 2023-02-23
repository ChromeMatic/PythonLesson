# guessing game
import random

attempts = 0
number = int(random.randint(1, 100))


def decrease_attempts():
    global attempts
    attempts -= 1


def easy_level():
    global attempts
    attempts = 10


def hard_level():
    global attempts
    attempts = 5


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
end_game = True


def guess_number(num):
    global number
    if num > number:
        decrease_attempts()
        return "high"
    elif num < number:
        decrease_attempts()
        return "low"
    elif num == number:
        return "win"


question = input("Choose a difficulty. Type 'easy' or 'hard': ")

if question == "easy":
    easy_level()
elif question == "hard":
    hard_level()
else:
    print("Invalid difficulty")

while end_game:
    print(f"You have {attempts} attempts remaining to guess the number.")
    ans = int(input("Make a guess : "))
    result = guess_number(num=ans)

    if result == "high":
        print("Too High")
    elif result == "low":
        print("Too Low")
    elif result == "win":
        print(f"You got it the answer was {number}")
        end_game = False

    if attempts <= 0:
        end_game = False
