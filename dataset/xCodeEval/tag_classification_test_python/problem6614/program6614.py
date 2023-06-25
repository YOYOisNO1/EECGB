def program6614():
    n,k = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    count = 0 
    for i in range(0,len(a)):
        if a[i]%2 == 0:
            count = count + 1
    if k-count <= n*8-sum(a):
        if k-count < n and k==n*4:
            print("NO")
        else:
            print('YES')
    else:print('NO')
    #hack:2 6\n2 2 2 2 2 6