    N, P = map(int, input().split())
    
def chk(k):
        x = N - k*P
        if x > 0 and sum(map(int, bin(x)[2:])) <= k <= x:
            return 1
        return 0
    
    for i in range(1, 100):
        if chk(i):
            print(i)
            break
    else:
        print(-1)
    