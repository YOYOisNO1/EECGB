    __author__ = 'Darren'
    
    
def solve():
        n = int(input())
        a, b, c, mod = 2, 2, 4, 1000000009
        while n > 2:
            a = (a << 1) % mod
            c = c * (a - 3) % mod
            b = (b + c) % mod
            n -= 2
        print((b * b + 1) * 2 % mod)
    
    
    if __name__ == '__main__':
        solve()