def program1128():
    n=input()
    s=n
    while n != 1:
        for i in range(n/2,0,-1):
            if not n%i:
                n = i
                break
        s+=n
    print s   