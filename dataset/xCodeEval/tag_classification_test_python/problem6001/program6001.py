def program6001():
    import math
    n = int(input())
    a = list(map(int, input().split()))
    pos = {}
    ans = []
    for i in range(n) :
    	pos[a[i]] = i
    	ans.append(0)
    a.sort()
    ans[pos[a[n - 1]]] = a[0]
    for i in range(n - 1) :
    	ans[pos[a[i]]] = a[i + 1]
    for i in ans :
    	print(i, end = ' ')