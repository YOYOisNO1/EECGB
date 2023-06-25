def program594():
    a = sorted(list(map(int, input().split())))
    if a[2] > 2 * (a[0] + a[1]):
    	a[2] = 2 * (a[0] + a[1])
    print(sum(a) // 3)