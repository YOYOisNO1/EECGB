    n, k, d = map(int, input().split())
    ans = {}
    
    
def dp_solve(n, k):
        if k == 0:
            return 0
        ans[0] = 1
        ans[1] = 1
        for i in range(2, n+1):
            cur_t = 0
            for j in range(1, k+1):
                if i-j >= 0:
                    cur_t += ans[i-j]
            ans[i] = cur_t
        return ans[n]
    
    
    a = dp_solve(n, k)
    b = dp_solve(n, d-1)
    # print(a, b)
    print((a-b) % int(1e9+7))