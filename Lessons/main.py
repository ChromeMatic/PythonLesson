# Lesson 2
# - Data types: integers, type, float, f string

# height = input("Please enter your height in m: ")
# weight = input("Please enter your weight in kg: ")
#
# H = float(height)
# W = int(weight)
# BMI = W / (H ** 2)
# result = int(BMI)
# print(f"Your BMI is {result}")

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
Bill = float(bill)

tip_percent = input("What percentage tip would you like to give? 10,12 or 15? ")
Tip_percent = (int(tip_percent)/100) + 1

amount = input("How many people to split the bill? ")
numbers = int(amount)

amount_for_each = (Bill / numbers) * Tip_percent
final_Bill = round(amount_for_each, 2)

final_amount = "{:.2f}".format(final_Bill)
print(f"Your bill is ${final_amount}")
