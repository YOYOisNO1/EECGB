def program674():
    from fractions import Fraction
    a,b,x,y=map(int,input().split())
    s=str(Fraction(x,y))
    n,i=len(s),0
    while(i<n and s[i]!='/'):
        i+=1
    if(i==n):
        x,y=int(s),1
    else:
        x,y=int(s[:i]),int(s[i+1:])
    print(min(int(a//x),int(b//y)))