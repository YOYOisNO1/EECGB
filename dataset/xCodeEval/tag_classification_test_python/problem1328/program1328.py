    import math
    import sys
    
    
    input = sys.stdin.readline
    
    
def main():
    
        n, k, m, d =  [int(x) for x in input().split(' ')]
    
        best = 0
    
        for i in range(1, d+1):
    
            # find the maxiumum x such that Arkady gets eaxctly d splittings
    
            pos = 1
    
            for j in range(100, -1, -1):
                jump = 2**j
    
                if pos + jump > m or pos + jump > n:
                    continue
    
                goes_into = n // ((pos + jump)*k)
                rem = 0
                if n % ((pos + jump) * k) >= pos+jump:
                    rem = 1
                if goes_into + rem >= i:
                    pos += jump
    
            goes_into = n // ((pos)*k)
            rem = 0
            if n % ((pos)*k) >= pos:
                rem = 1
    
            if pos <= m and goes_into + rem == i:
                best = max(best, pos * i)
    
        print(best)
    
    if __name__ == '__main__':
        main()