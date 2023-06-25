def program6500():
    """import math
    n,k=map(int,input().split())
    t=input()
    c=0
    temp=0
    for i in range(1,n):
        for j in range(0,n-i):
            if(t[j]==t[j+i]):
                c=c+1
            else:
                break
        if(c==n-i and c>temp):
            temp=c
        c=0
            #else:
                #if(c>temp):
                    #temp=c
                #c=0
                #break
    
    
    
    
    ans=t
    for i in range(0,k-1):
        ans=ans+t[temp:]
    #ans=n+(n-c)*(k-1)
    print(ans)"""
            
    """n=int(input())
    s=[int(x) for x in input().split()]
    temp=0
    c=1
    for i in range(1,len(s)):
        if(s[i]<=(2*s[i-1])):
            c=c+1
        else:
            if(c>temp):
                temp=c
            c=1
    
    if(c>temp):
        temp=c
    print(temp)"""
    
    
    """n=int(input())
    L=[]
    for i in range(0,n):
        l,r=map(int,input().split())
        L.append((l,r))
    o=0
    flag=0
    G1=[]
    G2=[]
    l=-1
    r=1000000007
    for i in range(0,n):
        for j in range(i+1,n):
            l1=L[i][0]
            r1=L[i][1]
            l2=L[j][0]
            r2=L[j][1]
            if((l1<=r1) and (l2<=r2) and ((l2<=l1 and r2<=r1 and l1<=r2) or (l1<=l2 and r1<=r2 and l2<=r1) or (l2>=l1 and r1>=r2) or (l2<=l1 and r1<=r2))):
                o=o+1
            else:
                flag=1
                G1.append(i)
                G2.append(j)
                break
    if(flag==0):
        temp=0
        for i in range(0,n):
            l=-1
            r=1000000007
            for j in range(0,n):
                if(j!=i):
                    l=max(l,L[j][0])
                    r=min(r,L[j][1])
            #print(l)
            #print(r)
            if((r-l)>temp):
                temp=r-l
        print(temp)
    else:
        G1=list(set(G1))
        G2=list(set(G2))
        if(len(G1)==1 and len(G2)>1):
            temp=0
            for i in range(0,n):
                l=-1
                r=1000000007
                for j in range(0,n):
                    if(i!=j and i!=G1[0] and j!=G1[0]):
                        l=max(l,L[j][0])
                        r=min(r,L[j][1])
                if((r-l)>temp):
                    temp=r-l
            print(temp)
        elif(len(G2)==1 and len(G1)>1):
            temp=0
            for i in range(0,n):
                l=-1
                r=1000000007
                for j in range(0,n):
                    if(i!=j and i!=G2[0] and j!=G2[0]):
                        l=max(l,L[j][0])
                        r=min(r,L[j][1])
                if((r-l)>temp):
                    temp=r-l
            print(temp)
        elif(len(G1)==1 and len(G2)==1):
            temp1=0
            for i in range(0,n):
                l=-1
                r=1000000007
                for j in range(0,n):
                    if(i!=j and i!=G1[0] and j!=G1[0]):
                        l=max(l,L[j][0])
                        r=min(r,L[j][1])
                if((r-l)>temp1):
                    temp1=r-l
    
            temp2=0
            for i in range(0,n):
                l=-1
                r=1000000007
                for j in range(0,n):
                    if(i!=j and i!=G2[0] and j!=G2[0]):
                        l=max(l,L[j][0])
                        r=min(r,L[j][1])
                if((r-l)>temp2):
                    temp2=r-l
            print(max(temp1,temp2))
        else:
            print(0)"""
    
    """n,k=map(int,input().split())
    s=[int(x) for x in input().split()]
    S=[]
    c=0
    for i in range(0,len(s)):
        S.append(str(s[i]))
    #print(S)
    for i in range(0,n):
        t1=S[i]
        for j in range(0,n):
            if(i!=j):
                t=int(t1+S[j])
                if(t%k==0):
                    #print((i+1,j+1))
                    c=c+1
    
    print(c)"""
                
    a,b=map(int,input().split())
    x,y,z=map(int,input().split())
    ansy=max(((2*x)+(y)-a),0)
    ansb=max(((y)+(3*z)-b),0)
    print(max(ansy+ansb,0))