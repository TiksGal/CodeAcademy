from dotenv import dotenv_values

config = dotenv_values(".env")

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == config["username"] and password == config["password"]:
        print("ACCESS GRANTED")
        break
    else:
        print("WRONG CREDENTIALS")