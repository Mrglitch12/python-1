# Function declaration
def login_system():
    # Stored user details
    username = "admin"
    password = "1234"
    is_verified = True
    attempts = 3

    while attempts > 0:
        entered_username = input("Enter Username: ")
        entered_password = input("Enter Password: ")

        if entered_username == username and entered_password == password:
            if is_verified:
                print(" Login Successful!")
            else:
                print(" Account is not verified.")
            return
        else:
            attempts -= 1
            print(" Invalid username or password.")
            print("Attempts left:", attempts)

    print(" Account locked. Too many failed attempts.")


# Call the function
login_system()