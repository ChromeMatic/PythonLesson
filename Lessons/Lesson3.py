# Love calculator
print("Welcome to the Love Calculator!")
name1 = input("Please enter your name: ").lower()
name2 = input("Please enter her name: ").lower()

combineString = name1+name2.lower()

t = combineString.count("t")
r = combineString.count("r")
u = combineString.count("u")
e = combineString.count("e")

true = t+r+u+e

L = combineString.count("l")
o = combineString.count("o")
v = combineString.count("v")
e = combineString.count("e")

love = L + o + v + e

result = int(str(true) + str(love))

if result < 10 | result > 90:
    print(f"Your score is **{result}**, you go together like coke and mentos")
elif result >= 40 & result <= 50:
    print(f"Your score is **{result}**, you are alright together.")
else:
    print(f"Your score is **{result}**")


