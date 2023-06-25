def program1633():
    password = input()
    cap = False
    sml = False
    dig = False
    ln = False
    if len(password) >= 5:
        for i in password:
            if i.isupper():
                cap = True
            if i.islower():
                sml = True
            if i in "1234567890":
                dig = True
            ln = True
    if dig == True and cap == True and sml == True and ln == True:
        print("Correct")
    else:
        print("Too weak")