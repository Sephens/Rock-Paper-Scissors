# import the module that will simulate computer choices

import random

# Rock smashes scissors.
# Paper covers rock.
# Scissors cut paper.

# Take in user input with input()
# Play several games in a row using a while loop
# Clean up your code with Enum and functions
# Define more complex rules with a dictionary

# Take User Input
user_action = input("Enter a choice ('R-rock' , 'S-Scissor', 'P-Paper'): ")

# Make the Computer Choose
# You can use random.choice() to have the computer randomly select between the actions:
possible_action = ["R", "P", "S"]
computer_action = random.choice(possible_action)

# You can also print the choices that the user and the computer made:
print("\n You chose {}, computer chose {} \n".format(user_action,computer_action))

# Determine a Winner
if computer_action == user_action:
    print("Both of you chose {} and it is a tie".format(user_action))
elif user_action == "R":
    if computer_action == "S":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers Rock. You lose!")
elif user_action == "P":
    if computer_action == "R":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "S":
    if computer_action == "P":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
