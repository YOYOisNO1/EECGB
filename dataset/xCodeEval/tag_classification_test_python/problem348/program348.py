def program348():
    cad = input()
    cad = cad[0] + cad[2] + cad[4] + cad[3] + cad[1]
    n = int(cad)
    ans = pow(n, 5, 100000)
    print('{:05d}'.format(ans))