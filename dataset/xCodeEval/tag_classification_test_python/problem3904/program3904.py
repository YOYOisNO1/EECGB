def program3904():
    n = int(input())
    n = [int(i) for i in str(n)]
    ans = 1
    if len(n)>2:
        ans *= 9**(len(n)-3)
        if not all([i==9 for i in n[3:]]):
            n[2] -= 1
        mult1 = (n[0]-1 if n[0] > 1 else 1) * 9 * 9
        mult2 = n[0] * (n[1]-1 if n[1] > 1 else 1) * 9
        mult3 = n[0] * n[1] * n[2]
        print(ans) * max(mult1, mult2,mult3)
    elif len(n) == 2:
        mult1 = (n[0]-1 if n[0] > 1 else 1) * 9
        mult2 = n[0] * n[1]
        print(str(ans) * max(mult1, mult2))
    else:
        print(n[0])