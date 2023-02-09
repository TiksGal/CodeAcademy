# Create a variables containing strings for username and password. 
# Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# 1
# username = "Marius"
# password = "secret"

# while True:
#     entered_username = input("Enter username: ")
#     entered_password = input("Enter password: ")

#     if entered_username == username and entered_password == password:
#         print(f"Welcome, {username}!")
#         break
#     else:
#         print("Try again.")

username, password = ["Marius", "secret"]

while (entered := input("Enter username and password: ").split())[0] != username or entered[1] != password:
    print("Incorrect username or password. Try again.")
else:
    print("Hi again!")

