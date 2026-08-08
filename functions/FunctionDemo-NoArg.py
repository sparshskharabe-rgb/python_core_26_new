# 1. Function Definition - Defining/Creating the function
# 2. Function Call - using it


# Function Definition - create a function
# No-argument function
def displayWelcomeScreen():
    print("\t\t\t\t\t\tWELCOME TO MY BANK")
    print("\t\t\t\t\t=================================")
    print("Kindly let us know how can we serve you !!! ")
    print("1. New Account Creation Request")
    print("2. Existing user ? Login ")
    print("3. Fund Transfer ")


# No-argument function
def userInput():
    # Accept user input
    choice = int(input("Please enter your selection (1-2) : "))  # user provided choice

    # Display the user choice
    print("User's choice is : ", choice)


# Function Call - Using teh function
if __name__ == '__main__':
    # Display the welcome screen
   displayWelcomeScreen()
   userInput()
