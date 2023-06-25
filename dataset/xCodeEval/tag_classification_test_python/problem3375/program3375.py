    import sys
def gcd(a,b):
        if a==0:
            return b
        return gcd(b,a%b)
        
    a,b = map(int, sys.stdin.readline().split())
    ii = a%b
    s = (a + ii)%b
    if s == 0:
        print("Yes")
    else:
        seen = {ii:1}
        while not (s in seen):
            
            if s == 0:
                print("Yes")
                break
            seen[s] = 1
            s = (s + s%b)%b
        if s in seen:
            print("No")
            