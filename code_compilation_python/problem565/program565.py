def program565():
    s = input()
    print(s.lower()) if (2 * (sum(1 for x in s if x.isupper()) < len(s)) else print(s.upper())