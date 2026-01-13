# A username validator script
# - Must be between 3 and 20 characters long
# - Should not contain spaces

username = input("Enter your username: ")
is_validlen = True if 20 > len(username) > 3 else False

if not is_validlen:
    print("The username must be between 3 and 20 characters long")
elif not username.find(" ") == -1:
    print("The username mustn't contain any spaces")
else:
    print(f"Welcome, {username}!")
