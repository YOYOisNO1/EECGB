    import sys
    input = sys.stdin.readline
    
    
def read_int():
        res = list(map(int, input().strip().split(" ")))
        return res[0]
    
    
def read_ints():
        res = list(map(int, input().strip().split(" ")))
        return res
    
    
def quick_pow(x, y, mo):
        res = 1
        while y > 0:
            if y % 2 == 1:
                res = res * x % mo
            x = x * x % mo
            y //= 2
        return res
    
    
def C(m, n, mo):
        if m < 0 or n < 0 or m < n:
            return 0
        n = min(n, m - n)
        down = 1
        up = 1
        for i in range(n):
            up = up * (m - i) % mo
            down = down * (i + 1) % mo
        return up * quick_pow(down, mo - 2, mo) % mo
    
    
def main(n, k):
        mo = int(1e9 + 7)
        if k >= n:
            return quick_pow(2, n, mo)
        else:
            res = 0
            x = 1
            for i in range(k + 1):
                res = (res + x) % mo
                x = x * (n - i) * quick_pow(i + 1, mo - 2, mo) % mo
            return res
    
    
    if __name__ == "__main__":
        n, k = read_ints()
        print(main(n, k))