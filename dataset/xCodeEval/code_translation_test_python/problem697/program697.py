def program697():
    arr = list(map(int, input().strip().split()))
    s = sum(arr)
    if s % 5 == 0 and s//5 > 0:
    	print(s//5)
    else:
    	print(-1)