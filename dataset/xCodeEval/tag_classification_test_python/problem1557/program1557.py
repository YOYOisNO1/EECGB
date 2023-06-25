def program1557():
    n=int(input())
    y=input()
    for i in range(1,n+1):
        if n%i==0:
            a=list(y[:i])
            a.reverse()
            y=''.join(a)+y[i:]
    print(y)