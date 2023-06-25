def main():
        a, ta = map(int, input().split())
        b, tb = map(int, input().split())
        h, m = map(int, input().split(':'))
        res, lo = 0, h * 60 + m - 300
        hi = lo + ta
        print(sum(max(lo, t) < min(hi, t + tb) for t in range(0, 1140, b)))
    
    
    if __name__ == '__main__':
        main()