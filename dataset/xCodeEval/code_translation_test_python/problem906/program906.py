    import math
    import random
    
    
def get(dtype=int):
        return dtype(input())
    
    
def array(dtype=int):
        return [dtype(num) for num in input().split()]
    
    
def solve_test_case():
        n, k = array()
        s = input()
        W = [ord(c) - ord('a') + 1 for c in s]
    
        W.sort()
    
        ans = [W[0]]
        m = W[0]
    
        i = 1
        no_pos = False
        # print(W)
    
        while len(ans) < k and i < n:
            if W[i] > m + 1:
                m = W[i]
                ans.append(m)
            i += 1
        if len(ans) < k:
            print(-1)
        else:
            print(sum(ans))
    
    
    n_test_cases = 1
    
    if n_test_cases == 0:
        n_test_cases = get()
    
    for i_test_case in range(n_test_cases):
        solve_test_case()