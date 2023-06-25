    import sys
    input = sys.stdin.readline
    
def multiply(arr):
        ret = 1
        for i in range(10):
            ret *= arr[i]
        return ret
    
    k = int(input())
    dic = []
    s = 'codeforces'
    res = ''
    
    if k == 1:
        print(s)
    
    else:
        rep = [1]*10
        m = 1
        idx = 0
    
        while True:
            rep[idx] += 1
            idx = (idx+1) % 10
            if multiply(rep) >= k:
                break
    
        for i in range(10):
            res += s[i]*rep[i]
        
        print(res)