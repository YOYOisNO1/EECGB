def program3733():
    n = input()
    res = ( (2*pow(4, n-1, 1000000007))%1000000007 + pow(2, n-1, 1000000007))%1000000007
    print res