def program1749():
    
    str1 = input()
    str2 = input()
    printy = False
    for i in range(len(str1)):
        a = str1[i]
        a = a.lower()
        b = str2[i]
        b = b.lower()
        if printy == False:
            if a > b:
                print(1)
                printy = True
            elif a < b:
                print(-1)
                printy = True
            else:
                pass
    if printy == False:
        print(0)