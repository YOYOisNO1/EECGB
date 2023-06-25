def program5908():
    from fractions import gcd
    n = int(input())
    crush = list(map(int,input().split()))
    was = [0] * n
    ans = 1
    for i in range(n):
        if was[i]:
            continue
        num = i
        j = 0
        while not was[num]:
            was[num] = 1
            num = crush[num] - 1
            j += 1
        if i != num:
            ans = -1
            break
        else:
            if j % 2 == 0:
                j //= 2
            ans = ans * j // gcd(ans,j)
    print(ans)