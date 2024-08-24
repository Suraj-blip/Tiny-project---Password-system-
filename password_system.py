# Initialize empty lists to store usernames and passwords


usernames = []
passwords = []



def sign_up():
    """
    Function to allow users to sign up with a new username and password.
    """
    print("Welcome to the sign up process!")

    # Get new username from user
    new_username = input("Please enter a new username: ")

    # Check if username already exists
    if new_username in usernames:
        print("Sorry, that username is already taken. Please choose a different one.")
        return

    # Get new password from user
    new_password = input("Please enter a new password: ")

    # Add new username and password to the lists
    usernames.append(new_username)
    passwords.append(new_password)

    print("Sign up successful! You can now log in.")
    start()

def log_in():
    """
    Function to allow users to log in with their username and password.
    """
    print("Welcome to the login process!")

    # Get username from user
    username = input("Please enter your username: ")

    # Check if username exists in the list
    if username not in usernames:
        print("Sorry, that username does not exist. Please try again.")
        return

    # Get password from user
    password = input("Please enter your password: ")

    # Check if password matches the stored password
    location_usrname = usernames.index(username)
    if password != passwords[location_usrname]:
        print("Incorrect password. Please try again.")
        #return
        log_in()

    print("Login successful! Welcome back,", username)

def start():
    """
    Main function to run the sign up and login processes.
    """
    while True:  # Keep asking for input until valid
        try:
            choice = int(input("Enter '1' for sign up and '2' for login: "))
            break  # Exit loop if input is valid
        except ValueError:
            print("Invalid input. Please enter a number.")

    if choice == 1:
        sign_up()
    elif choice == 2:
        log_in()
    else:
        print("Invalid choice. Please try again.")
        start()  # Recursively call start() for invalid choices

start()  # Start the sign up and login process