def program2839():
    n=int(input())
    s=input()
    l=list(s)
    x=[]
    X=[]
    a,b=0,0
    for i in range(n):
        if(l[i]=='x'):
            a+=1
            x.append(i)
        else:
            b+=1
            X.append(i)
    
    
    if(a>b):
        t= int(n/2) - b
        ans1=t
        for i in x:
            if(t>0):
                l[i]='X'
                t-=1
    
    elif(b>a):
        t=int(n/2) - a
        ans1=t
        for i in X:
            if(t>0):
                l[i]='x'
                t-=1
    ans=''
    for i in range(n):
        ans+=l[i]
    
    if(a==b):
        #print("enter1")
        print(0)
        print(ans)
    else:
        #print("enter1")
        print(ans1)
        print(ans)
    