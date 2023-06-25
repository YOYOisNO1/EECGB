def program2961():
    a=input()
    if a[0]==a[0].lower() and a[1:]==a[1:].upper():
        print(a[0].upper()+a[1:].lower())
    elif a[0]==a[0].upper() and a[1:]==a[1:].upper():
        print(a[0].lower()+a[1:].lower())
    else:
        print(a)