def program897():
    __author__ = 'Esfandiar'
    n = int(input())
    res = n
    while n:
        f=1
        for i in range(2,n//2+1):
            if n % i == 0:
                res+= n // i
                n//=i
                f=0
                break
        if f:res+=1;break
    print(res)
    
    