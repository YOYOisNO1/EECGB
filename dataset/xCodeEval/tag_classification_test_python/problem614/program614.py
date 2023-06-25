    n = int(input())
    
def good(n):
        s = set()
        for i in range(4):
            s.add(n%10)
            n //= 10
        return len(s)==4
    
    n += 1
    while True:
        if good(n):
            print(n)
            break
        n += 1