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
    pw=1
    for i in range(len(n)-1, -1, -1):
        res=(res+pw*int(n[i]))%m
        pw=(pw*10)%m
    
    partial=res
    
    for x in n:
        if (int(x)!=0):
            res=min(res, partial)
        partial=(partial-int(x)*pow(10, len(n)-1, m))%m
        partial=(partial*10+int(x))%m
        if (partial<0):
            partial+=m
    print(res)