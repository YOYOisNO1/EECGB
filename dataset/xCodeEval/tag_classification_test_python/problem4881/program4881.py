    import sys
    import math
    import bisect
    import itertools
    import random
    import re
    
def solve(n, k):
        for i in range(k + 1):
            m = n - i
            total = k - i * 2
            if 3 * m <= total and total <= 5 * m:
                return i
        return -1
    
def main():
        n, k = map(int, input().split())
        ans = solve(n, k)
        print(ans)
    
    if __name__ == "__main__":
        main()