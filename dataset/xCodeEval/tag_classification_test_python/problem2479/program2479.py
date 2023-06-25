    ##n = int(input())
    ##a = list(map(int, input().split()))
    ##print(" ".join(map(str, res)))
    
def get(s):
        n = len(s)
        res = []
        i = 0
        while i < n:
            while i < n and s[i] == '_':
                i += 1
            j = i
            while j < n and s[j] != '_':
                j += 1
            if j != i: 
                res.append(j-i)
            i = j
        return res
    
    n = int(input())
    s = list(input())
    
    lmax = 0
    cnt = 0
    i = 0
    while i < n:
        j = i
        while j < n and s[j] != '(':
            j += 1
        ss = get(s[i:j])
        for e in ss:
            lmax = max(lmax, e)
        if j < n and s[j] == '(':
            k = j;
            while k < n and s[k] != ')':
                k += 1
            ss = get(s[j+1:k])        
            cnt += len(ss)
            j = k+1
        i = j
    print(lmax, cnt)