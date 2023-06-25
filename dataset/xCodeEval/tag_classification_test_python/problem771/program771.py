def program771():
    from ipaddress import ip_address
    
    
    for _ in range(int(input())):
        x=int(input())
        a=[int(x) for x in input().split()]
        d=[0,0,0]
        while(x!=0):
            d[x-1]=1
            x=a[x-1]
        if(sum(d)==3):
            print('YES')
        else:
            print("NO")