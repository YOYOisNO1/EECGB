def program2735():
    n, m = tuple(map(int, input().strip().split()))
    b = tuple(map(int, input().strip().split()))
    
    res = [0]*m
    
    
    for b_i in b:
        for i in range(b_i-1, n):
            if res[i]==0:
                res[i] = b_i
    
    print(' '.join(map(str,res)))