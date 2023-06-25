def program4466():
    a = sorted(map(int, input().split()))
    b = 0
    while a[1] > 1 and a[0] > 0:
    	a[1] -= 2
    	a[0] += 1
    	a.sort()
    	b += 1
    print(b)