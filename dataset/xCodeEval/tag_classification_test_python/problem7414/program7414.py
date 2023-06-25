def main():
        from math import floor
        m = int(input())
        lo, hi = max(7, m * 247 // 50), (m + 10) * 249 // 50
        l = [float(x * x * x) for x in xrange(2, 170416)]
        while lo + 1 < hi:
            mid = (hi + lo) * .5
            t = sum(floor(mid / x) for x in l)
            if t < m:
                lo = int(mid)
            else:
                hi = int(mid)
        mid = float(hi)
        print(hi if sum(floor(mid / x) for x in l) == m else -1)
    
    
    if __name__ == '__main__':
        main()