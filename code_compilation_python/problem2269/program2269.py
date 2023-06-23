    from sys import stdin, stdout
    
    
def count(n):
        d = {}
        cnt = 0
        cur = 0
        
        for i in range(n + 1):
            for j in range(n - i + 1):
                for z in range(n - j - i + 1):
                    v = i * 1 + j * 5 + z * 10 + (n - i - j - z) * 50
                    
                    if not v in d:
                        d[v] = 1
                        cur += 1
                    else:
                        d[v] += 1
        
        return cur
    
    n = int(stdin.readline())
    
    for i in range(20, 200):
        n = i
        
        if count(i) != count(20) + 49 * (i - 20):
            print(i)
    
    if n >= 20:
        upp = count(20) + 49 * (n - 20)
    else:
        upp = count(n)
    print(upp)