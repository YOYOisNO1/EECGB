def program4852():
    a,b = map(int,input().split())
    res = (a*(a+1)/2*b + a)*(b*(b-1)/2)
    print(res%1000000007)