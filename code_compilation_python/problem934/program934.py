def func(n, a, b):
        if a > n:
            return
        val = 2 ** (n - a - 1)
        if b >= val:
            func(n, a + 1, b - val)
            print(a, end = " ")
        else:
            print(a, end = " ")
            func(n, a + 1, b)
    
    
def main():
        n, m = map(int, input().split())
        func(n, 1, m - 1)
    
    
    
    if __name__ == '__main__':
        main()
    