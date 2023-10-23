def is_uppercase(text):
    for symbol in text:
        if symbol.isalpha() and symbol.islower():
            return False
    return True


def is_uppercase(text):
    lowercase_letters = [symbol
                         for symbol in text
                         if symbol.isalpha() and symbol.islower()]
    return not bool(lowercase_letters)


def is_uppercase(text):
    return text.upper() == text


# def is_uppercase(text):
#     return text.isupper()


assert is_uppercase("c") == False
assert is_uppercase("C") == True
assert is_uppercase("hello I AM DONALD") == False
assert is_uppercase("HELLO I AM DONALD") == True
assert is_uppercase("$%&") == True
