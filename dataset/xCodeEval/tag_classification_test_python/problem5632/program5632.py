def program5632():
    N, M = map(int, input().split())
    if N > M:
    	N,M = M, N
    ans = 0;
    if N >= 3:
    	ans = (N * M + 1) / 2
    elif N == 1:
    	ans = M
    else:
    	ans = M / 4 * 4
    	if M % 4 >= 2:
    		ans += 4
    	elif M % 4 == 1:
    		ans += 2
    print(ans)