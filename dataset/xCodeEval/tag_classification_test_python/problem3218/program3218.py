def program3218():
    n = input()
    t=len(n)
    if(t>1):
        n1=n[0].upper()
        n2=n[1:-1]
        n1+=n2
        n3=n[-1]
        n1+=n3
        print(n1)
    else:
        n1=n[0].upper()
        print(n1)