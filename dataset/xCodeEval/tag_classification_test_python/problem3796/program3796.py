def program3796():
    n=int(input())
    if n<0:
        n=n*(-1)
        a=str(n)
        z=n
        z=z//(100)
        if z!=0:
            s="-"+str(z)
        elif n%10!=0:
                s="-"
        else:
            s=""
        if n%10>(n//10)%10:
            print(s+a[-2])
        else:
            print(s+a[-1])
    else: print(n)