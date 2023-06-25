def program3764():
    s=input()
    y=list(s)
    y.reverse()
    x=list(s)
    f=0
    for i in x:
        for j in range(len(s)+1):
            a=s[:j]+i+s[j:]
            y=list(a)
            y.reverse()
            x=list(a)
            if x==y:
                print(a)
                f=1
                break
        if f:
            break
    if f==0:
        print("NA")