def palindrome(string):
    if not isinstance(string,str):
        raise TypeError("Palindrome is only defined for strings.")
    string = string.lower()
    return string == string[::-1]