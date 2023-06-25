    x,y,a,b = map(int,input().strip().split())
    
def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
def lcm(a, b):
        return (a * b) / gcd(a, b)
    j = lcm(x,y)
    n1 = a//j + 1
    if (n1-1)*j < a:
        n1 += 1
    n2 = b//j + 1
    if (n2-1)*j > b:
        n2 -= 1
    print(int(n2 - n1 + 1))