privileged_users = ['Alice', 'Bob', 'Charlie']
user = input("Enter your name: ")

if user in privileged_users:
    print(f"Hello, {user}. Welcome back! You are a privileged user.")
else:
    print(f"Welcome, {user}.")
