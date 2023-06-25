    mod = 10**9+7
    
def countWays(arr, m, N,d): 
        count = [0 for i in range(N + 1)] 
        count[0] = 1
        for i in range(1, N + 1): 
            for j in range(m): 
                if (i >= arr[j]) and arr[j]<d:   
                    count[i] += count[i - arr[j]]
                count[i]%=mod
        return count[N]
    
def countWays1(arr, m, N): 
        count = [0 for i in range(N + 1)] 
        count[0] = 1
        for i in range(1, N + 1): 
            for j in range(m): 
                if (i >= arr[j]):  
                    count[i] += count[i - arr[j]]
            count[i]%=mod
        return count[N]
    n,k,d = map(int,input().split())
    a = [i for i in range(1,k+1)]
    t1  = countWays(a,len(a),n,d)
    t2 = countWays1(a,len(a),n)
    print((t2-t1+mod)%mod)