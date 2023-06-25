    import sys
    input = sys.stdin.readline
     
def main():
        n = int(input())
     
        ans = 4 * n
        for a in range(1, 10**5 + 1):
            ans = min(ans, a + (n + a - 1) // a)
     
        print(ans)
     
    main()