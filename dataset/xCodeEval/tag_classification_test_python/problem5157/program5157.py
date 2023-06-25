def srch(x, prec, prec1, poz, h):
    
        a = x // 2
        r = x % 2
    
        if prec < poz <= prec + 2 ** h - 1:
            return srch(x // 2, prec, prec1, poz, h - 1)
    
        if poz == prec + 2 ** h:
            return prec1 + x // 2 + (x % 2)
    
        if prec + 2 ** h < poz <= prec + 2 ** (h + 1) - 1:
            return srch(x // 2, prec + 2 ** h, prec1 + x // 2 + x % 2, poz, h - 1)
    
    
    s = input()
    ls = s.split()
    
    n = int(ls[0])
    l = int(ls[1])
    r = int(ls[2])
    
    if n == 0:
        print(0)
        quit()
    
    if n == 1:
        print(1)
        quit()
    
    kn = 0
    aux = 1
    
    while aux * 2 <= n:
        aux *= 2
        kn += 1
    
    if l == 1:
        lnr = 0
    else:
        lnr = srch(n, 0, 0, l - 1, kn) # nr de analizat, numarul de elemente precedente, numarul de 1 precedenti, pozitia de cautat, inaltimea pasului curent
    rnr = srch(n, 0, 0, r, kn)
    
    print(rnr - lnr)