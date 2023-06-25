def cal(m,n,i):
        tot=1
        for j in range(1,n-i+1):
            tot=tot*(n*m-m-n+i+j)/(n*m-n+i+j)
        for j in range(1,i+1):
            tot=tot*(m-i+j)/(n*m-n+j)
        for j in range(1,i+1):
            tot=tot/j*(n-i+j)
        return tot
    
    
    n,m = input().split()
    n = int(n)
    m = int(m)
    ans = 0
    
    for i in range(1, min(n,m)+1):
        ans += i * i /n * cal(m,n,i)
    
    print(ans)