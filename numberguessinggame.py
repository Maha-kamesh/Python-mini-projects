from random import randint
from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
turns=0
def check_answer(user_guess,actual_number,turns):

    if user_guess<actual_number:
        print("Too low!\n Guess again")
        return turns-1

    elif user_guess>actual_number:
        print("Too high!\n Guess again")
        return turns-1
    else:
        print(f"You got it! The number was {actual_number}")


def set_difficultly():
    difficulty=input("Choose a difficulty level.Type 'Easy' or 'Hard': ").lower()
    if difficulty == "Easy":
       return EASY_LEVEL_TURNS
    else:
       return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100." )

    number = randint(1,100)

    turns=set_difficultly()

    Guess=0
    while Guess!=number:
        print(f"You have {turns} attempts remaining to guess the number.")
        Guess=int(input("Guess the number: "))

        turns=check_answer(Guess,number,turns)
        if turns==0:
            print("You've run out of guesses!,You lose")
            return

game()
