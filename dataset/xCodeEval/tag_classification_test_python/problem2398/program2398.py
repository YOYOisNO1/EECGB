def program2398():
    n=input()
    a=n.count("4")
    b=n.count("7")
    if a==0 and b==0:
        print(-1)
    elif a>=b:
        print(4)
    else:
        print(7)
            