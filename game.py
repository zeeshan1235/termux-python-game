import random
print("GitHub Updated Version - Number Guessing Game!")
number = random.randint(1, 10)
try:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print("You won!")
    else:
        print(f"You lost! The number was {number}")
except ValueError:
    print("Please enter a valid number.")
