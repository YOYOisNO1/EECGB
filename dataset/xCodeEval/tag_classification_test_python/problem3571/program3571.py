def program3571():
    k=input()
    x=map(int,k.split())
    t=x[1]
    n=x[0]
    s=input()
    while(t>0):
        i=0
        while(i<n-1):
            if s[i]=='B' and s[i+1]=='G':
                x=s[i+2:]
                s=s[:i]+s[i+1]+s[i]
                s=s+x
                i+=1
            i+=1
        t-=1
    print(s)