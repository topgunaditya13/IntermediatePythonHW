def password_validator():
    unique_characters = ['!', '^', '?', '+', '*']
    while True:
        password = input("Please enter a password: ")
        if "!" in password:
            print("Password Worked!")
        elif "'^'" in password:
            print("Password worked!")
        elif "?" in password:
            print("Password Worked!")
        elif "'+'" in password:
            print("Password worked!")
        elif "*" in password:
            print("Password Worked!")
        else:
            print("Password Invalid Suckaaaaaaaaaaaaaaaaa!")
            password = input("This ass gets a second chance:")
