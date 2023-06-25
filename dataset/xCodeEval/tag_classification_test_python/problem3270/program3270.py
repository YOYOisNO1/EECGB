def program3270():
    n=int(input())
    q=list(input())
    
    i=0
    c=[]
    s=0
    while(i<n):
        if(q[i]=='1'):
            s=s+1
        else:
            c.append(s)
            s=0
        i=i+1
    
    c.append(s)
    for i in range(len(c)):
        print(c[i],end='')
        