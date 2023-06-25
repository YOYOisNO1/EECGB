def help(arr):
        l=len(arr)
        ans=0
        for i in range(l):
            ans+=arr[i]*(10**(l-1-i))
        return ans
    
    
    m,s=map(int,input().split())
    d=s
    k=s
    arr=[1]+[0]*(m-1)
    k-=1
    i=0
    while(k>0 and i<m):
        while(arr[i]<9 and k>0):
            arr[i]+=1
            k-=1
        i+=1
    a=help(arr)
    arr=[0]*(m-1)+[1]
    s=s-1
    i=0
    while(i<m and s>0):
        while(arr[i]<9 and s>0):
            arr[i]+=1
            s-=1
        i+=1
    
    arr=list(reversed(arr))
    b=help(arr)
    if d>9*m:
        a=-1
        b=-1
    if d==0:
        if m==1:
            a=0
            b=0
        else:
            a=-1
            b=-1
    
    print(b,a)