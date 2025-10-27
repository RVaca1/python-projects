# number guessing game

import string
import random
import sys

nums = string.digits
nums2 = string.digits




def run_loop_game():


    goal_guessed = random.randint(0,100)


    guess = int(input("Guess a number in the range of 0 to 100\n"))
    tries = 5
    while tries > 0:
        if guess < goal_guessed:
            print("Guess is too low\n")
            tries -= 1

            guess = int(input("Guess a number in the range of 0 to 100\n"))
        elif guess > goal_guessed:
            print("Guess is too high\n")
            tries -= 1

            guess = int(input("Guess a number in the range of 0 to 100\n"))
        elif guess == goal_guessed:
            print("Guess is correct!\n")
            break


    else:
        print(f"The guess was {goal_guessed} you had only 5 chances")
        restart = input("Want to restart ? (y/n)")
        if restart == 'y':
            tries = 5
            print(restart)

            run_loop_game()
        else:
            sys.exit()

run_loop_game()







