    # import math
    # from collections import defaultdict
    
    
def gint():
        return map(int, input().split())
    
    
def main():
        n, m, a, b = gint()
        if b > m * a:
            return n * a
    
        if m > n and n * a > b:
            return b
    
        res = b * (n / m)
        if (n % m) * a < b:
            res += (n % m) * a
        else:
            res += b
        return res
    
    print(main())