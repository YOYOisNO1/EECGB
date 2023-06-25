def program258():
    N, M = map(int, input().split())
    ans = -1
    min = N // 2
    if N % 2 != 0:
    	min += 1
    for i in range(min, N+1):
    	if i % M == 0:
    		ans = i
    		break
    print(ans)