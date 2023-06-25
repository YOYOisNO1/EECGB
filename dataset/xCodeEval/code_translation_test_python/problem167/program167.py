def program167():
    a = input()
    if a[:1].islower() == True and a[1:].isupper():
        print(a[:1].upper()) + a[1:].lower()
    elif a.isupper() == True:
        print(a.lower())
    elif len(a) == 1 and a.islower() == True:
        print(a.upper())
    else:
        print(a)