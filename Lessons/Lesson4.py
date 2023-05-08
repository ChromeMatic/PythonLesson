# Python
# List, random module
# import random
#
# num = random.randint(1, 2000)
# num2 = random.random() * 5
#
# print(f"Random number is {num}")
# print(f"Random decimal number between 0 and 5 = {num2}")

import random

states = ["test1", "test2", "test3"]

print(states[0])

states[0] = "for honer"

# add one element to the list
states.append("test2_7")

# add multiple to a list
states.extend(["test24", "test25", "test26"])

# get size of list
sizeOfList = len(states)

print(states)

num = random.randint(0, 4)

print(num)

# Choice function from the random module
# picks a random index and display it.
print(random.choice(states))

# jaaden kyrellle
