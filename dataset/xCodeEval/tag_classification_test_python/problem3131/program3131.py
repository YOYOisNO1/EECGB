    # cook your dish here
# def f(k):
    #     if k==1:
    #         return 1
    #     return (4 * f(k-1))**2
    
# def ans(k):
    #     return 6*f(k)
    
def ans2(k, prev):
        return 6 * prev;
    
    MOD = 10**9 +7
    
    k = int(input())
    
    prev = 1
    for i in range(k-1):
        prev =  ((4 * prev)**2)%MOD
    
    res= ans2(k, prev)%MOD
    print(res)
    