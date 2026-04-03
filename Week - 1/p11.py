import random

num = random.randint(1, 100)
flag = False
i = 0
while not flag:
    guess = int(input("Guess the number (between 1 and 100): "))
    if guess < num:
        print("Too low! Try again.")
        i += 1
    elif guess > num:
        print("Too high! Try again.")
        i += 1
    else:
        print("Congratulations! You've guessed the number.")
        flag = True
print("Game Over you took", i, "attempts to guess the number.")