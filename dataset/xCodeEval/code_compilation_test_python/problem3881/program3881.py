    import fractions
    string =input()
    A = string.split()
    a=int(A[0])
    b=int(A[1])
    x=int(A[2])
    y=int(A[3])
    m= max(x,y)
    cnt=0
    if gcd(x,y)%x ==0 AND gcd(x,y)%y ==0:
        x = fractions.gcd(x,y)/x
        y = fractions.gcd(x,y)/y
    for i in range (1, m):
        if x*i<= a:
            if y*i<=b:
                cnt = cnt+1
    print cnt    
def gcd(a, b):
        while b:
            a, b = b, a%b
        return a