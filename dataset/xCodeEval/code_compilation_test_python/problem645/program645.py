def program645():
    n,m = map(int,input().split())
    
    l = sorted(list(map(int,input().split())))
    for i in range(m - n - 1):
        print(min([l[i+n-1]-l[i]))