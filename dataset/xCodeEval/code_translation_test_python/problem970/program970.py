def program970():
    import sys
    input = sys.stdin.readline
    n = int(input())
    s = [0]+list(map(int, input().split()))
    ret = 9876543210
    for xth in range(1, len(s)):
        summ = 0
        for i in range(1, len(s)):
            summ += 2*(abs(xth-i)+(i-1)+(xth-1))*s[i]
        ret=min(ret, summ)
    print(ret)