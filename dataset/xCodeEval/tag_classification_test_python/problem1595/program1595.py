def program1595():
    N, X = map(int, input().split())
    cnt = 0
    for i in range(1, N+1):
    	if X % i == 0:
    		if X // i <= N: cnt += 1
    print(cnt)