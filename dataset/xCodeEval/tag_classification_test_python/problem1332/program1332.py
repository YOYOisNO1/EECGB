def program1332():
    var = input().split()
    m = int(var[0])
    n = int(var[1])
    
    if (m % 2 == 0) or (n % 2 == 0):
        print((m*n)/2)
    elif m == 1 and n != 1:
        print((n-1)/2)
    elif n == 1 and m != 1:
        print((m-1)/2)
    else:
        print(() m*(n-1) + (m-1))/2