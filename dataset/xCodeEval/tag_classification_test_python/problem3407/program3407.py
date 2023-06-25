    import sys
    import math
    import bisect
    import itertools
    import random
    import re
    
def main():
        n = int(input())
        A = list(map(int, input().split()))
        B = []
        s = set()
        for i in range(1, n):
            B.append(A[i] - A[i-1])
        min_val = 10 ** 18
        for i in range(1, len(B)):
            C = []
            for j in range(len(B)):
                if j == i - 1:
                    continue
                elif j == i:
                    C.append(B[j-1] + B[j])
                else:
                    C.append(B[j])
            val = max(C)
            min_val = min(min_val, val)
        print(min_val)
    
    if __name__ == "__main__":
        main()