def program1262():
    b=int(input())
    g=int(input())
    n=int(input())
    if n<=b and n<=g:
        print(n+1)
    else:
        if n<=b and n>g:
            print(g+1)
        elif n<=g and n>b:
            print(b+1)
        else:
            print(g+b-n+1)