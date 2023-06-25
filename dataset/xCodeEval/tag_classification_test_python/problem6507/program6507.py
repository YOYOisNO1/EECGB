    # cook your dish here
    # cook your dish here
    import sys
    import math
    import random
    import heapq
    #sys.setrecursionlimit(10**6)
    input=sys.stdin.readline
def pow(a,n,m):
        if n==0:
            return 1 
        x=pow(a,n//2,m)
        if n%2==0 :
            return (x*x)%m
        else:
            return (x*x*a)%m
     
def gcd(a,b):
        while b!=0:
            a,b=b,a%b
        return a 
        
def bs(arr,le,ri):
        l=0
        arr.sort()
        r=len(arr)-1
        ans=10000000
        while l<=r:
            m=(l+r)//2
            if arr[m]>=le and arr[m]<=ri:
                ans=arr[m]
                r=m-1
            elif arr[m]<le:
                l=m+1 
            else:
                r=m-1
        return ans
def dfs(al,l,p,n,le,pa):
        l[n]=le
        p[n]=pa 
        for i in al[n]:
            if i!=pa:
                dfs(al,l,p,i,le+1,n)
                
def lca(al,l,p,x,y):
        if l[x]>l[y]:
            x,y=y,x 
        d=l[y]-l[x]
        while d!=0:
            y=p[y]
            d-=1
        while x!=y:
            x=p[x]
            y=p[y]
        return x
        
def dfs1(al,i,x,y,vis,p,ans):
        vis[i]=1 
        if i==x or i==y:
            p=1 
        ans[i]=p 
        for j in al[i]:
            if vis[j]==0:
                dfs1(al,j,x,y,vis,p,ans)
            
    # l=[1]*1000001 
    # l[0]=0 
    # l[1]=0 
    # for i in range(2,1001):
    #     if l[i]==1 :
    #         j=i 
    #         while j*i <=1000000:
    #             l[j*i]=0 
    #             j+=1
    # p=[]
    # for i in range(2,1000001):
    #     if l[i]==1:
    #         p.append(i)
    # ls=[]
    # for i in p:
    #     if i*i<=1000000:
    #         ls.append(i)
    # print(len(ls))
    
    t=1
    # t=int(input())
    while t>0:
        # n=int(input())
        n,m=map(int,input().split()) 
        p=[0]
        c=1
        c1=0
        l=[0]*(21*m)
        while c<=20:
            for j in range(1,m+1):
                if l[c*j]==0:
                    l[c*j]=1
                    c1+=1
            c+=1 
            p.append(c1)
        c=1
        ls=[0]*(n+1)
        for i in range(2,n+1):
            if ls[i]==0:
                c1=1
                temp=i
                    # print(c)
                while temp*i<=n:
                    temp*=i
                    c1+=1
                    ls[temp]=1
                c+=p[c1]
        print(c)        
        t-=1# cook your dish here