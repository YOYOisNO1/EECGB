def main():
        n = hi = int(input())
        lo = 1
        while lo  < hi:
            mid, x, c = (lo + hi) // 2, n, 0
            while x > mid:
                x -= mid
                c += 1
                x -= x // 10
            if (c * mid + x) * 2 < n:
                lo = mid+1
            else:
                hi = mid
            prn(lo, hi)
        print(hi)
    
    
    if __name__ == '__main__':
        main()