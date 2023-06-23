def program1100():
    n = input("n:")
    n = int(n)
    if n%2 == 0:
        a = n/2 - 1
        b = n/2 + 1
    else:
       a = (n-1)/2
       b = (n+1)/2
    print a
    print b