def program3474():
    N, L, R, X = map(int, input().split())
    C = map(int, input().split())
    Ans = 0
    
    for Cf in range(1, 1 << N):
    	V = [C[i] for i in range(N) if Cf & (1 << i) > 0]
    	if max(V) - min(V) >= X and L <= sum(V) and sum(V) <= R:
    		Ans += 1
    
    print Ans