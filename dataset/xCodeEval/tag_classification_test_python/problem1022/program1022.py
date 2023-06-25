    from itertools import *
    
def min_wins(A, B):
        not_win = [(0, 2), (0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]
        ans = float('inf')
        for p in permutations(range(6)):
            a, b = A[:], B[:]
            li = [not_win[i] for i in p]
            for i,j in li:
                mn = min(a[i], b[j])
                a[i] -= mn
                b[j] -= mn
            cur = max_wins(a, b)
            ans = min(cur, ans)
        return ans
def max_wins(A, B):
        ## max wins for player owning first Array
        mx = 0
        for i in range(3):
            mn = min(A[i], B[(i+1)%3])
            mx += mn
        return mx
def solve(A, B, n):
        ## alice max wins
        mxa = max_wins(A, B)
        ## alice min wins
        mna = min_wins(A, B)
    
        print(mna, mxa)
    
    n = int(input())
    alice = list(map(int, input().split()))
    bob = list(map(int, input().split()))
    
    solve(alice, bob, n)