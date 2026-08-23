from handlers.loginhandler import LoginHandler
from exceptions.loginexception import LoginException

# Entry point of your application. Main script

def promptForLogin():
    print("Please enter you credentials to proceed further.")
    username = input("Username : ")    # user provided info
    password = input("Password : ")    # user provided info

    # Check if user and pass are not empty
    if len(username.strip()) == 0:
        print("Invalid Username")
        return
    if len(password.strip()) == 0:
        print("Invalid Password")
        return
    
    print(username, password)

    # Delegate the request to handler
    # Controller 
    response = LoginHandler.handle_login(username, password)
    print(response)
    if response is None:
        try:
            #print("Invalid Credentials. Either username or password is incorrect")
            raise LoginException("Invalid Credentials. Either username or password is incorrect")
        except LoginException as e:
            print("Exception Reported", e.__class__)



    else:
        if response[2] == 0:
            #Display the customer dashboard
            print("You are successfully logged in as a customer. ")
            # Dispaly the customer menu option with other details
        elif response[2] == 1:
            #Display the admin dashboard
            print("You are successfully logged in as a admin. ")
            # Dispaly the admin menu option with other details

def newaccountrequest():
    print("New Account Request")

def fundtransfer():
    print("Fund Transfer")


if __name__ == '__main__':
    print("\t\t\t\t\t\tWELCOME TO MY BANK")
    print("\t\t\t\t\t=================================")
    print("Kindly let us know how can we serve you !!! ")
    print("1. New Account Creation Request")
    print("2. Existing user ? Login ")
    print("3. Fund Transfer ")

    choice = int(input("Please enter your selection (1-2) : "))   # user provided choice
    
    if choice == 1:
        newaccountrequest()
    elif choice == 2:
        promptForLogin()
    if choice == 3:
        fundtransfer()


