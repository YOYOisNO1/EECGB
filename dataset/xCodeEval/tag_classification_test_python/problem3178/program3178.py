    import sys
    import math
    import bisect
    import itertools
    import random
    
def main():
        A = list(map(int, input().split()))
        d = dict()
        for a in A:
            if a not in d:
                d[a] = 0
            d[a] += 1
        min_val = sum(A)
        for a in d:
            if d[a] >= 2:
                val = sum(A) - a * 2
                min_val = min(min_val, val)
            if d[a] >= 3:
                val = sum(A) - a * 3
                min_val = min(min_val, val)
        print(min_val)
    
    if __name__ == "__main__":
        main()