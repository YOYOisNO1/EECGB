def program2691():
    N = int(input())
    P = [0 for _ in range(1000010)]
    # store the largest prime factor of a number --> if number is prime, mark its multiples
    for i in range(2, N):
        if P[i] == 0:
            for j in range(2*i, N+1, i):
                P[j] = i
    for i in range(N-P[N]+1, N+1):
        ans = min(ans, i-P[i]+1)
    print(ans)