def program3712():
    s = input()
    res = pow(2, len(s)-1)*(int(s, 2))
    print res%1000000007