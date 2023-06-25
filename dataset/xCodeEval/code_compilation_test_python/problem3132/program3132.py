def power(3,n):
        p=1
        for i in range(n):
            p=p*3
        return p
def ans(n):
        return power(n-2)*n*(n-1)
    n=int(input())
    print(ans(n))