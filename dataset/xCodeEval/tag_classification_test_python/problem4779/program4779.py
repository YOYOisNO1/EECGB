def program4779():
    n = (int)(input())
    flag = True
    a = list(map(int,input().split()))
    a.sort()
    for x in range(1,len(a)):
        if a[x] < 2 *a[x-1] and a[x] != a[x-1]:
            print('YES')
            flag = False
            break
    if flag:
        print('NO')