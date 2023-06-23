def program1661():
    n=int(input())
    x=0
    while(n):
        x+=n%10
        n=n/10
    return x
        