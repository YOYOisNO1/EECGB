def gcd(a,b):
        while b > 0:
            a, b = b, a % b
        return a
        
def lcm(a, b):
        return a * b // gcd(a, b)
    
    T, W, B = map(int, input().split())
    LCM = lcm(W, B)
    
    ANS = T//LCM
    REQ = ANS * min(W, B)
    REQ = REQ+min(W, B)-1
    C = ANS * LCM
    C += min(W, B)-1
    ANS = REQ - max(0, C-T)
    
    GCD = gcd(int(ANS), int(T))
    NUM, DENOM = (ANS//GCD), (T//GCD)
    
    print(int(NUM), end = "")
    print("/", end = "")
    print(int(DENOM))