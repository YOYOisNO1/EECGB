def program4848():
    a, b= map(int, input().split())
    res = b*(b-1)/2*(a+b*a*(a+1)/2)
    print(res%(10**9+7))
    