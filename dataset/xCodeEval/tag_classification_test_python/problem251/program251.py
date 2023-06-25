def program251():
    a=input()
    k=0
    t=0
    for i in a:
        if i.islower():
            t+=1
        else:
            k+=1
    if t>=k:
        print(a.lower())
    else:
        print(a.upper())