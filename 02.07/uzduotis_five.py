# import random

# target = random.randint(1, 10)
# guess = 0

# while guess != target:
#     guess = int(input("Guess a number from 1 to 10: "))
#     if guess < target:
#       print("Too low! Try again.")
#     elif guess > target:
#       print("Too high! Try again.")
#     else:
#       print("You got it! The number was", target)

# import random

# target = random.randint(1, 10)
# tries = 0

# while tries < 3:
#     guess = int(input("Guess a number from 1 to 10: "))
#     tries += 1
#     if guess == target:
#         print("You got it! The number was", target)
#         break
#     elif guess < target:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")

# if tries == 3:
#     print("You have exhausted all your tries. The number was", target)

import random

target = random.randint(1, 10)
tries = 0
guess = None

for i in range(3):
    guess = int(input("Guess a number from 1 to 10: "))
    if guess == target:
        print("You got it! The number was", target)
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != target:
    print("You have exhausted all your tries. The number was", target)
