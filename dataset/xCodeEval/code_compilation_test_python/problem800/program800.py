def program800():
    import math
    n,m,t = map(int,input().split())
    nn = n-4
    mm = m-1
    s = mm+nn
    tt = t-5
    return m*(math.factorial(n)/(24*math.factorial(nn)))*(math.factorial(s)/(math.factorial(tt)*math.factorial(s-tt))