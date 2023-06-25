def program3661():
    n=str(input())
    l=len(n)
    n=int(n)
    a=((n//(10**(l-1)))+1)*(10**(l-1))
    print(a-n)