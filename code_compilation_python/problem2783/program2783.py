def program2783():
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    c1=0 
    c2=0
    for i in range(0,n-1):
        if a[i]%2==0:
            c1+=1 
        elif a[i]%2!=0:
            c2+=1 
        if c1==c2 and c1!=0:
            b.append(abs(a[i]-a[i+1]))
        b=sorted(b)
        sum=0
        for items in b:
            if items+sum<=b:
                sum+=items 
        print(sum)