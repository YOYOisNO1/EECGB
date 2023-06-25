    ones = [1]
    for i in range(1, 52):
        ones.append(ones[-1] * 10 + 1)
    
    
def solve(n, cache={}):
        if n == 0: return 0
        if n in cache: return cache[n]
    
        x = None
        for v in ones:
            if v <= n:
                x = v
    
        y = x * 10 + 1
        res1 = (n // x) * len(str(x)) + solve(n % x)
        res2 = len(str(y)) + solve((y - n) % x) + ((y - n) // x) * len(str(x))
        
        cache[n] = min(res1, res2)
        return cache[n]
    
    
def main():
        n = int(input())
        print(solve(n))
    
    
    if __name__ == '__main__':
        main()