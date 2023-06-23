    import sys
    sys.setrecursionlimit(600)
    
    
    
    M = 998244353
    
    
    
    MAXNUM = 512
    factor = [1]*(MAXNUM+2)
    factor[-1]=0
    
    for i in range(1,MAXNUM+1):
        factor[i] = (factor[i-1]*i)%M
    
def fastfrac(a,b):
        numb = pow(b,M-2,M)
        return ((a%M)*(numb%M))%M
    
def comb(n,k):
        if n<k: return 0
        if n==k: return 1
        num1 = factor[n]
        num2 = factor[k]
        num3 = factor[n-k]
        num = (num2*num3)%M
        return fastfrac(num1,num)
    
    
    
    
    n, x = map(int,input().split())
    
    
    store = [[0 for j in range(n+1)] for i in range(n+1)]
    
    
    for p in range(n+1):
        for q in range(n+1):
            store[p][q] = pow(p,q,M)
    
        
    
    
    
    
    
    
    dic = {}
def getnext(restn,restx):
    
        if (restn,restx) in dic:  return dic[(restn,restx)]
        if restn==2:  return restx
    
    
        if restx < restn:
            return store[restx][restn]
    
        output = store[restn-1][restn]
        for sub in range(2,restn+1):
            temp = getnext(sub,restx-(restn-1))*comb(restn,sub) % M
            temp *= store[restn-1][restn-sub]
            output += temp
    
            output = output % M
    
        dic[(restn,restx)] = output 
        return output 
    
    
    
    
    ans = getnext(n,x)
    
    
    print(ans) 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    