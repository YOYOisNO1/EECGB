    n = int(input())
    crush = [int(x)-1 for x in input().split(" ")]
    perdimos = False
    tomados = [False]*n
    numeritos = []
    cadena = []
    for i in xrange(n):
        if not tomados[i]:
            c = i
            while c not in cadena and not tomados[c]:
                cadena.append(c)
                c = crush[c]
            if c == cadena[0]:
                if len(cadena) % 2 == 0:
                    numeritos.append(len(cadena)/2)
                else :
                    numeritos.append(len(cadena))
                for d in cadena:
                    tomados[d] = True
            else:
                perdimos = True
                break
        cadena = []
def gcd(a, b):
        while b:      
            a, b = b, a % b
        return a
    
def lcm(a, b):
        return a * b // gcd(a, b)
    
def lcmm(*args):
        return reduce(lcm, args)
    if perdimos:
        print(-1)
    else :
        print(reduce(lcm,) numeritos)
            