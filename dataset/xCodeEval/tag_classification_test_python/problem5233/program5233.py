def program5233():
    #Bhargey Mehta (Junior)
    #DA-IICT, Gandhinagar
    import sys, math, queue, bisect
    #sys.stdin = open("input.txt", "r")
    MOD = 10**9+7
    sys.setrecursionlimit(1000000)
    
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for ai in a:
        ans += abs(ai)
    print(ans)