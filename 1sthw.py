# at least 8 characters
# at least one unique character

def password_validator():
    unique_characters = ['!', '^', '?', '+', '*']
    hasUniqueCharacter = False
    while True:
        password = input("Please enter a password: ")
        "IL!keDogs3"
# checking if unique characters are in password
        for char in password:
            if char in unique_characters:
                hasUniqueCharacter = True
        if len(password) < 8 or hasUniqueCharacter is False:
            password = input("Please enter a password: ")
        else:
            break
    print("Sucess! password is valid. ")
