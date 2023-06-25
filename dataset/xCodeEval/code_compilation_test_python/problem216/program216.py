def program216():
    x = int(input())
    a = []
    b = []
    for i in range(1,x+1):
        a.append(i)
    for j in range(0,x):
        b.append(pow(a[j],j))
    print(sum(b)%(x+1))