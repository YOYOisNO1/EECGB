def program1301():
    n,m,k=map(int,input().split())
    s=k%2
    r=(k-1)//(2*m)
    d=r*m+1
    i=d*2
    d=1
    if s==1:
        i-=1
    while i!=k:
        i+=2
        d+=1
    if s==1:
        s='L'
    else:
        s='R'
    print(r+1,d,s)