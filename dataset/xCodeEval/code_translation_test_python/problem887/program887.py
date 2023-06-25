    import sys
    import math
    import bisect
    
def solve(s):
        n = len(s)
        min_val = n
        for i in range(1, n):
            if i * 2 <= n:
                if s[0:i] == s[i:2*i]:
                    val = i + 1 + (n - 2 * i)
                    min_val = min(min_val, val)
        return min_val
    
def main():
        n = int(input())
        s = input()
        print(solve(s))
    
    if __name__ == "__main__":
        main()