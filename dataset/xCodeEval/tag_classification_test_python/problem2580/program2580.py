def program2580():
    x = input().split()
    n = int(x[0])
    a = int(x[1])
    b = int(x[2])
    l=[0]*n
    for i in range(1,n):
        l[i]=min(a/i,b/(n-i))
    print(max(l))