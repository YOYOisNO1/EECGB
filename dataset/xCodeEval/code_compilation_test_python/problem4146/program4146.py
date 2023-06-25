    n=input()
    m=int(input())
    
def pow(a, b, m):
        res=1
        while b:
            if (b%2==1):
                res=(res*a)%m
            a=(a*a)%m
            b/=2
        return res
    
    res=0
    for x in n:
        res=(res+int(x))%m
    partial=res
    
    for x in n:
        partial=(partial-int(x)*pow(10, len(n)-1, m))%m
        partial=(partial*10+int(x))%m
        res=min(res, partial)
    print(res)