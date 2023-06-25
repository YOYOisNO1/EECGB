def program6269():
    n = input()
    if n==0:
        print(1)
    else:
        res = ( (2*pow(4, n-1, 1000000007))%1000000007 + pow(2, n-1, 1000000007))%1000000007
        print(res)