    from math import gcd 
def com(x, y, l, r) : 
        lcm = (x * y) // gcd(x, y) 
        count1 = (l - 1) // lcm 
        countr = r // lcm 
        return countr - count1 
    n,m,z=[int(x) for x in input().split(" ")]
    print(com(n,m,1,z))