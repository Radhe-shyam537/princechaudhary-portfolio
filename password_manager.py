# simple_password_manager.py
# Python Password Manager - Beginner Friendly

import hashlib
import json
import os

FILE_NAME = "users.json"

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Load users from JSON file
def load_users():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return {}

# Save users to JSON file
def save_users(users):
    with open(FILE_NAME, "w") as f:
        json.dump(users, f, indent=4)

# Add new user
def add_user(username, password):
    users = load_users()
    if username in users:
        print("User already exists!")
        return False
    users[username] = hash_password(password)
    save_users(users)
    print(f"User '{username}' added successfully!")
    return True

# Verify user login
def verify_user(username, password):
    users = load_users()
    if username not in users:
        return False
    return users[username] == hash_password(password)

# List all users (for demo purposes)
def list_users():
    users = load_users()
    if not users:
        print("No users found!")
        return
    print("\nAll Users:")
    for user in users:
        print("-", user)

# Main interactive CLI
def main():
    print("🔐 Welcome to Simple Python Password Manager 🔐")
    while True:
        print("\nOptions:")
        print("1. Add User")
        print("2. Verify User")
        print("3. List Users")
        print("4. Exit")
        choice = input("Enter choice (1-4): ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if verify_user(username, password):
                print("✅ Login successful!")
            else:
                print("❌ Login failed!")
        elif choice == "3":
            list_users()
        elif choice == "4":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
