def program7045():
    n=input()
    i=1
    s=0
    while True:
        p=(n)/(2*i)
        if p==0:
            break
        s+=(i*p)
        if((n)%(2*i)==i):
            s+=(n-i)
        i*=2
    print(s)