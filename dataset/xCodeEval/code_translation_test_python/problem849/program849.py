def program849():
    n=input()
    a=int(n)
    l=len(n)
    x=a//10**(l-1)
    print((10**(l-1))*(x+1)-a)