def solve(x,n):
        if n==1:return 0
        return x*(n/2)+solve(x+x,(n+1)/2)
    n=input()
    print(solve(1,n))