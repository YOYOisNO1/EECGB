def program4871():
    N = int(input())
    
    mx = N // 2
    for i in range(1, len(str(N)) + 1):
        m = int('9' * i)
        if m <= N:
            mx = m
    
    S = lambda x: sum([int(i) for i in str(x)])
    print(str(S(mx) + S(N - mx)))