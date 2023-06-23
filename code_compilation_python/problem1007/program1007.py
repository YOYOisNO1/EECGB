def program1007():
    n, k = input().split(' ')
    n = int(n)
    k = int(k)
    coef1 = k*k-k+2.25-2*n
    if coef1 < 0:
        print('-1')
    elif coef1 == 0:
        n1 = n % 10
        k1 = k % 10
        coef1 = (k1*k1-k1+2.25-2*n1)**0.5
        coef2 = k-0.5
        coef = coef2-coef1
        if coef % 1 == 0:
            print(int(coef))
        else:
            print(int(coef)+1)
    else:
        coef1 = coef1**0.5
        coef2 = k-0.5
        coef = coef2-coef1
        if coef % 1 == 0:
            print(int(coef))
        else:
            print(int(coef)+1)