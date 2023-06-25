def main():
        n, m = map(int, input().split())
        if n == 1 == m:
            res = 1.
        else:
            res = (2 * n * m - n - m) / (n * m - 1) / n
    
        print('{:.16f}'.format(res))
    
    
    if __name__ == '__main__':
        main()