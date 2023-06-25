def program1636():
    a=input()
    if(len(a)>=5):
        f1=False
        f2=False
        f3=False
        for i in range(len(a)):
            if(65<=ord(a[i])<=90):
                f1=True
            elif(97<=ord(a[i])<=122):
                f2=True
            elif(48<=ord(a[i])<=57):
                f3=True
        if(f1 and f2 and f3):print("Correct")
        else:print("Too weak")
    else:print("Too weak")    