    
    x = [int(i) for i in input().split()]
    
def gcd(a,b):
    	r = 0
        while b > 0:
            r = a%b
            a = b
            b = r
        return a
        
def lcm(a, b):
        return a * b / gcd(a, b)
    
    
    t=x[2]//lcm(x[0],x[1])
    print(t)