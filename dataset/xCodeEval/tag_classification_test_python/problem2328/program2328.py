def program2328():
    a=[]
    for i in range(3):
        a.append(list(map(int,input().split())))
    print((sum(a[2])+sum(a[1])-sum(a[0]))//2,a[0][1],a[0][2])
    print(a[1][0],(sum(a[2])+sum(a[0])-sum(a[1]))//2,a[1][2])
    print(a[2][0],a[2][1],(sum(a[1])+sum(a[0])-sum(a[2]))//2)