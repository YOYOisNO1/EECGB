    import io,os
    from math import gcd
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    
    dic = [{} for _ in range(100001)]
    
    
    for i in range(2,100001):
    
        curr = i - 1
        for key in dic[i]:  curr -= dic[i][key]
        dic[i][1] = curr 
    
        for j in range(2*i,100001,i):
            dic[j][j//i] = curr
    
    
    #print(dic[:13])
    
    
def main(t):
    
    
        n = int(input())
    
        M = 10 ** 9 + 7
        ans = 0
        for i in range(1,n):
            for key in dic[n-i]:
                l = key*i//gcd(key,i)
                ans += l * dic[n-i][key]
                ans %= M
    
    
    
        print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    T = 1 #int(input())
    t = 1
    while t<=T:
        main(t)
        t += 1