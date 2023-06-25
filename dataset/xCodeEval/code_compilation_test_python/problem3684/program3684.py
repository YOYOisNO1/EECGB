def program3684():
    s = input()
    if s.upper() == s or s[1:].upper() == s[1:]: print s.swapcase()
    else print s