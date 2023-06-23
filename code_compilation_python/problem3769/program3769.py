def reversive(number, modulo):
        return pow(number, modulo - 2, modulo)
    
    
def congr(a, b, p, x):
        c = [list() for i in range(p + 1)]
        for i in range(0, p - 1):
            c[pow(a, i, p)].append(i)
        s = 0
        for n1 in range(1, p):
            k = reversive(n1, p) * b % p
            for j in range(len(c[k])):
                n2 = c[k][j]
                y0 = n1
                y1 = ((n2 - n1) + p - 1) % (p - 1)
                n = y0 + y1 * p
                s += (x - n + (p - 1) * p) // ((p - 1) * p)
        return s
    
    
    a, b, p, x = [int(j) for j in input().split()]
    print(congr(a, b, p, x))