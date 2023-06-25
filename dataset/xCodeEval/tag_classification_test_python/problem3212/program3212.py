def program3212():
    import math; a = int(input());sum = 0
    for i in range(2, a):
        t = a
        while t != 0:
            sum += t%i;t //= i
    d = math.gcd(sum, a-2)
    print(str(sum//d)+'/'+str((a-2)//d))