# Write a terminal program that required user to login. If user does not have an account he should register. 
# credentials are username and password. Store the information in the file txt or pickle. 
# Validate user credentials from the file. Once user has logged in: print text: "Hello, <username>".

def register():
    with open("credentials.txt", "a") as file:
        username = input("Enter a new username: ")
        password = input("Enter a new password: ")
        file.write(f"{username},{password}\n")
        print("Account created successfully!")

def login():
    with open("credentials.txt", "r") as file:
        lines = file.readlines()
        credentials = [line.strip().split(",") for line in lines]
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        for cred in credentials:
            if cred[0] == username and cred[1] == password:
                return True, username
        return False, None

def main():
    print("Welcome to the Terminal Login Program!")
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")
    if choice == "1":
        register()
    elif choice == "2":
        success, username = login()
        if success:
            print(f"Hello, {username}!")
        else:
            print("Invalid credentials. Please try again.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
