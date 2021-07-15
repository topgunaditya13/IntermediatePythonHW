# Let's start by defining a function; password_validator:#
def password_validator():
    unique_characters=['!', '^', '?', '+', '*'] #This part is giving a list of unique characters that the computer stores; which we can later use to validate a password
    has_unique_character=False #Setting the value of a variable unique characters to false#
    while True:
        password=input("Please enter a password") #Asking for Input#
        for char in password: #For loop that is scanning each character in input#
            if char in unique_characters: #Conditional#
                hasUniqueCharacter=True #Setting this value to true now that there is a unique character#
                if len(password) >= 8 and hasUniqueCharacter is True: #Nested conditional#
                    break
                    print("SUCESS")
            else: #Anything besides these conditions will make this conditional true.#
                password = input("Please enter a valid password")
password_validator()     
