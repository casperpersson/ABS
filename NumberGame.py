# this is a guess the number game.
import random

print("Hello. What is your name?")
name = input()
secretNumber = random.randint(1, 20)
print("Well, " + name + ", i am thinking of a number between 1 and 20")

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print("take a guess.")
    guess = int(input())
    if guess < secretNumber:
        print("your guess is too low.")
    elif guess > secretNumber:
        print("your guess is too high")
    else:
        break  # this condition is the correct guess!

if guess == secretNumber:
    print("Good job, " + name + "! You guessed my number in " + str(guessesTaken) + " guesses")
else:
    print("Nope. the number i was thinking of was " + str(secretNumber))
