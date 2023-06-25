def gcd(p, q):
        if(q == 0):
            return p
        else:
            return gcd(q, p % q)
        
    
    if __name__ == "__main__":
        t = int(input())
        while t > 0:
            k = int(input())
            print(100 // gcd(k, 100))
            t -= 1