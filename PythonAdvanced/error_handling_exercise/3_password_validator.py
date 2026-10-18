class PasswordTooShortError(Exception):
    pass

class PasswordTooCommonError(Exception):
    pass

class PasswordNoSpecialCharactersError(Exception):
    pass

class PasswordContainsSpacesError(Exception):
    pass

PWD_VALID_LENGTH = 8
SPECIAL_CHARACTERS = ["@", "*", "&", "%"]

def pwd_too_common(pwd, special_chars):
    only_digits = pwd.isdigit()
    only_letters = pwd.isalpha()
    only_special = all(ch in special_chars for ch in pwd)

    return only_digits or only_letters or only_special



while True:
    password = input()

    if password == "Done":
        break

    if len(password) < PWD_VALID_LENGTH:
        raise PasswordTooShortError("Password must contain at least 8 characters")

    if pwd_too_common(password, SPECIAL_CHARACTERS):
        raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

    if not any(ch in SPECIAL_CHARACTERS for ch in password):
        raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

    if " " in password:
        raise PasswordContainsSpacesError("Password must not contain empty spaces")

    print("Password is valid" )







