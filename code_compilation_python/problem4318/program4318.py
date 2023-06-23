    par = map(int, input().split(" "))
    a, b, x, y = par[0], par[1], par[2], par[3]
    
def gcd(a, b):
        if b == 0:
            return a
        a,b = b, a%b
        return gcd(a,b)
    
    if a < b:
        a, b = b, a
        x, y = y, x
    #(a+1)//(x-1)
    sol = 1
    while a > 0 or b > 0:
        if sol % x == 0:
            if sol % y != 0:
                #print sol, "y"
                b -= 1
        else:
            #print sol, "x"
            a -= 1
        sol += 1
    print sol-1
        
            