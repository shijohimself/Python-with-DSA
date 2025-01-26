# guessing game
# generate a random int b/w 1 to 100 
import random

jackpot = random.randint(1,100)



i = 0
while True:
    num = int(input("num = "))
    if num == jackpot:
        print("You won!!")
        break
    elif num > jackpot:
        print("Guess something less")
    elif num < jackpot:
        print("guess something more")
    i += 1
    