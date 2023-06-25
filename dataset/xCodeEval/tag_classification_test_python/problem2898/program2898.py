def program2898():
    n=input()
    
    f=1
    a=map(int,input().split())
    d=a[1]-a[0]
    for i in range(n-1):
        if a[i+1]-a[i]!=d:
            f=0
            break
    
    print(a[-1]+d*f)