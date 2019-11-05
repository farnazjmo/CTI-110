# This program allows the user to choose to play random number guessing game
# from a menu or exit. The random number is in range of 1-100
# 11.04.19
# CTI-110 P5HW1 - Random Number
# Farnaz Jeddi Moghaddam

import random
# Constants for the menu choices
PLAY_GAME_CHOICE=1
EXIT_CHOICE=2

# The random number generator function
def random_number():
    return random.randint(1,100)

# The main function   
def main():
    # The choice varibale controls the loop
    # and holds the user's menu choice.
    choice=0
    
    while choice != EXIT_CHOICE:
        # Display the menu.
        display_menu()

        # Get the user's choice.
        choice=int(input('Enter your choice: '))

        # Call game function for playing game
        if choice== PLAY_GAME_CHOICE:
            guess_game()
# Perform the guess game until the user guesses the correct number.
def guess_game():
    random=random_number()
    # number_guesses holds the number of guesses the user makes.
    number_guesses=0
    while True:
        try:
            guess=int(input("Guess what the number is: "))
            # Number of guesses increases for each guess
            number_guesses=number_guesses+1
            if guess==random:
                print("Congratulations! You guessed the number with ", number_guesses, "guesses!")
                break
            elif guess>random:
                print("Too high, try again.")
            elif guess<random:
                print("Too low, try again.")
        except ValueError:
            print("Input must be an integer value!")
# The display_menu function displays the main menu.
def display_menu():
    print("MAIN MENU\n----------")
    print("1) Play Game")
    print("2) Exit")


# Call the main function.
main()
