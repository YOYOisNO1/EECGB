def program718():
    n,l,r = list(map(int,input().split()))
    count,cnt = 0,0
    lst = []
    lst1 = []
    for i in range(n-l+1):
        lst.append(1)
    for i in range(l-1):
        lst.append((1<<i+1))
    for i in range(r):
        lst1.append((1<<i))
    for i in range(n-r):
        lst1.append(lst1[-1])
    print(sum(lst),sum(lst1))