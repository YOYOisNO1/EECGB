    small_prime = [0]*(10**6+1)
    for i in range(2,10**6+1):
        if small_prime[i] != 0:
            continue
        small_prime[i] = i
        for j in range(1,10**6+1):
            temp = i*j
            if temp>10**6:
                break
            small_prime[temp] = i
    
def find(X):
        # find all prime 
        org = X
        P = set([])
        while small_prime[X] != X:
            P.add(small_prime[X])
            X = X//small_prime[X]
        P.add(X)
        P = sorted(list(P))
        Mp = P[-1]
        if Mp == org:
            return X
        return org-Mp+1
    
def find_ans(X):
        X1 = find(X)
        ans = X
        for x1 in range(X1,X):
            ans = min(ans,find(x1))
        return ans
    
    print(find_ans(int(input())))