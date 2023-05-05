#!/usr/bin/env python3

def validate_user(username, minlen):
    if type(username) != str:
        raise TypeError("username must be a string")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    # Username can't begin with a number
    if username[0].isnumeric():
        return False
    return True

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

