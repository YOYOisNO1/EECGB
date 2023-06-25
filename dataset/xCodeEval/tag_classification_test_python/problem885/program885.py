def program885():
    n=int(input())
    if n&1:
        print((n+1)/2)
    else:
        if n==0:
            print(0)
        else:
            print(n+1)