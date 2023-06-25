def program1028():
    
    n=int(input())
    a=list(map(int,input().split(' ')))
    b=list(map(int,input().split(' ')))
    
    
    mx=min(a[0],b[1])+min(a[1],b[2])+min(a[2],b[0])
    
    mn=max(a[0]-(b[2]+b[0]),0)+max(a[1]-(b[0]+b[1]),0)+max(a[2]-(b[1]+b[2]),0)
    
    print(mn,mx)