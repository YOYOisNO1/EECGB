def program3813():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    m = int(input())
    if m <= n:
    	print(sum(arr[:m]))
    else:
    	print(sum(arr) - d * (m-n))