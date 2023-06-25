def program2802():
    n = int(input()) % 6
    pp = int(input())
    for p in [0, 1, 2]:
        # print('#')
        ans = p
        q = 1
        while n >= q:
            # print(p)
            if q % 2 == 0:
                if p in (1, 2):
                    p = 3 - p
            else:
                if p in (0, 1):
                    p = 1 - p
            q += 1
        if p == pp:
            break
    print(ans)