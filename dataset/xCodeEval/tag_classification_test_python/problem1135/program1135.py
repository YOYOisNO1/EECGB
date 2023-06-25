def program1135():
    n,p,k=map(int,input().split())
    r=k/(2*p)
    if r*2*p!=k:
        r+=1
    dc=k%(2*p)
    if dc==0:
        dc=2*p
    if k%2==0:
        r2=dc/2
        ch='R'
    else:
        r2=dc/2+1
        ch='L'
    print(r,r2,ch)
    
        