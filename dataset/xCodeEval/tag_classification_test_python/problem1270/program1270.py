def read(func=int, is_list=False):
        if is_list:
            return map(func, input().split())
        else:
            return func(input())
    
    t, s, q = read(int, True)
    ans = 0
    while s < t:
        s = s * q
        ans += 1
    print(ans)
    