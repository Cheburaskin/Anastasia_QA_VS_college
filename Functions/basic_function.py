def is_valid_email(email):
    """Checks if the provided email address is valid.
    A valid email address must contain "@" and "." characters.
    """
    #return True if "@" in email and "." in email else False
    if "@" in email and "." in email and email.count("@") == 1 and email.index("@") < email.rindex("."):
        return True
    return False

input_email = input("Please enter your email address: ")
if is_valid_email(input_email):
    print("The email address is valid.")
else:
    print("The email address is invalid.")