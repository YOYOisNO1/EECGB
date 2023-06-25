    # http://codeforces.com/problemset/problem/768/B
    import math, copy
    
def module():
        global li
    
        i = 0
        while i < len(li):
            if li[i] not in [0, 1]:
                a = math.floor(li[i] / 2)
                b = li[i] % 2
    
                li.insert(i, a)
                li[i + 1] = b
                li.insert(i + 2, a)
    
                # print(li)
    
                i += 3
            else:
                i += 1
    
        end = 1
        for i in range(len(li)):
            if li[i] not in [0, 1]:
                end = 0
                break
            else:
                continue
    
        if end == 0:
            module()
        else:
            return
    
    n, l, r = map(int, input().split())
    li = [n]
    ans = 0
    
    module()
    for i in range(l - 1, r):
        ans += li[i]
    
    print(ans)