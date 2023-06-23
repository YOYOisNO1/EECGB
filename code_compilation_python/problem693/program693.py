def program693():
    n = int(input())
    m = int(n**0.5)+2
    ans = n
    for i in range(2,m):
        if n%i==0:
            ans = i
            break
    if ans==n:
        print(n)
    else:
        p =  ans
        x = [1 for i in range(p)]
        for i in range(ans+1, m):
            if n%i==0:
                if n//i>=p:
                    x = [0 for j in range(p)]
                    break
                else:
                    for j in range(1,n//i+1):
                        p[(j*i)%p] = 0
        print(max(x.count(1)), 1))
    
    
    
    
    