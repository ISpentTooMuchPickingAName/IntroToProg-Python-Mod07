# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrating Pickling and Structured Error Handling
# ChangeLog (Who,When,What):
# DPetkov,5.30.2023,Created script to complete assignment 07
# ---------------------------------------------------------------------------- #

guess = None  # Create a global variable
import pickle  # Import code from another module

# Create a list of responses so each is unique depending on which answer the user selects
list_of_things = ['Nope', 'So Close', 'Winner!...oh no...(dramatic pause)', 'Loser', 'Ouch']


def SoreLoser():  # Creates a binary file and writes the 'password' to it in binary
    print("\nGambler: This can't be.. I simply cannot lose, if you want my money you will need to")
    print("use a jedi mind trick to guess my ultra secret password to get my $10\n")
    file = open('SecretFile', 'ab')  # Open the file in binary append mode
    password = "Password"
    pickle.dump(password, file)  # Store contents inside the file
    file.close()  # Close the file
    return


def CounterProductive():  # Function is run when the user makes an invalid input to a y or n question
    raise TypeError  # Raise a specific error when this function is run


def JediMindTrick():  # The user chooses to trick the gambler to win the money
    file = open('SecretFile', 'rb')  # Open the file in binary read mode
    read = pickle.load(file)  # Read file contents
    print("\nGambler: I will give you the password. My password is:", read)  # Print file contents
    file.close()
    return


try:
    guess = abs(int(input("Gambler: Bet $10 you can pick my lucky number? Select any number between 1 and 10: "))) - 1
    # Absolute value in case the user wants to get smart and type a negative number
    # Use int() to turn the string into an integer, subtract 1 since the list index begins with 0
    if guess > 9:  # If user inputs anything over than 10, remember, guess -=1
        raise Exception  # Raise the specific exception routine
    elif guess == 2:  # if user guesses 3
        print("\nGambler: Annnnd...", list_of_things[guess])  # Read the list item in the selected index
        SoreLoser()  # Run function
        trick = input("The Game: Would you like to perform a jedi mind trick? [y/n]: ")  # User has to select y or n
        if trick.lower() == 'y':  # User selects y
            JediMindTrick()  # Run this function
        elif trick.lower() == 'n':  # User selects n
            print("\nThe Developer: You are truly a noble one, may the force be with you")
        else:  # User makes an invalid input
            print("\nThe Game: You had a mishap and jedi mind tricked yourself!\n")
            CounterProductive()
    else:  # Any guess between 1 and 10 that isn't the lucky number
        print("\nGambler: Annnnd...", list_of_things[guess])

except IndexError as IndErr:  # User selects any number 6 - 10
    print("\nGambler: Tough luck pal, next time...")

except ValueError as ValErr:  # User guesses a none integer
    print("""
    The Game:
    You were supposed to pick a number buddy
    You never had a chance :(
    """)

except TypeError as TypErr:  # User types a value that is neither y or n
    print("Gambler: Oh, why thank you for giving me $20! Bet was only $10 but I'll take it!")

except Exception as ExcErr:  # User guesses value over 10
    print("\nGambler: ... Everything ok in your head? I said 1 to 10 and you give me", guess + 1, "?")

except:  # Generic exception for any failure not covered in the other exception routines
    print("The Developer: Oh you really broke the game...")
