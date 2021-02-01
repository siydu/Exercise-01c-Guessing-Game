#!/usr/bin/env python3
import sys, random
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"



number = random.randrange(1,16)
count = 0
guess = -1
while guess != number:
    count = count + 1
    guess = input("Guess a number from 1 to 15: ")
    try:
        guess = int(guess)
        if guess != number:
            print("Not quite, please try again!")
    except:
        print("Please enter a number!")
print("Great job! You got it! You were able to guess the number in " + str(count) + " tries.")