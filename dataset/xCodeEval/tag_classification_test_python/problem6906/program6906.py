def solve(a, b, m):
        if a == b:
            return [a]
    
        for _len in range(2, 51):
            l = (a + 1) * (2 ** (_len - 2))
            r = (a + m) * (2 ** (_len - 2))
            if b < l or b > r: continue
    
            res = []
            res += [a]
    
            s = a
    
            for i in range(1, _len-1):
                L = 0
                R = m + 1
                while R - L > 1:
                    M = int((L + R) // 2)
                    l = (s + s + M + 1) * 2 ** (_len - i - 2)
                    r = (s + s + M + m) * 2 ** (_len - i - 2)
                    if r < b:
                        L = M
                    else:
                        R = M
    
                x = s + R
                res += [x]
                s += x
            res+=[b]
    
            return res
    
    tc = int(input())
    for _ in range(tc):
        a, b, m = map(int, input().split())
        res = solve(a, b, m)
        if res:
            print(len(res), end=' ')
            for i in res:
                print(i, end=' ')
            print()
        else:
            print(-1)