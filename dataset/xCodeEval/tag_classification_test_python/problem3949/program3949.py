    M, N = map(int, input().split())
    used = {}
    
def check(K):
        while K:
            KP = 0
            while K:
                if K%M==0:
                    K /= M
                elif K%M==1 and KP not in used:
                    K = (K-1)/M
                else:
                    return False
                KP += 1
        return True
    
    
    while N:
        if check(N):
            break
        P = 0
        while M ** P < N:
            P += 1
    
        high = M**P
        low = M**(P-1) if P else 0
    
        if P in used and (P-1) in used:
            print("NO")
            exit()
    
        elif P in used:
            used[P-1] = True
            N = N - low
    
        elif P-1 in used:
            used[P] = True
            N = high - N
    
        else:
            if high-N < N:
                used[P] = True
                N = high-N
            else:
                used[P-1] = True
                N = N-low
    
    
    print("YES")