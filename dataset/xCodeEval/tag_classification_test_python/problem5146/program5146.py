def get_ans(k):
        global mod
        if k == 1:
            ans[0] = 1
        elif k > 0:
            if k == 2:
                mod = 0
            get_ans(k // 2)
            ans.append(2 * ans[-1] + k % 2)
            steps.append(2 * steps[-1] + 1)
            mods.append(k % 2)
    
    
def get(k):
        global mod
        if k == 0 or k == -1:
            return 0
        if k == 1:
            return 1
        if k == 2:
            return 1 + mod
        else:
            l = 0
            r = len(steps)
            while r > l + 1:
                m = (r + l) // 2
                if steps[m] > k:
                    r = m
                else:
                    l = m
            if k == steps[l]:
                return ans[l]
            else:
                return ans[l] + get(k - steps[l] - 1) + mods[l + 1]
            
            
    
    
    n, l, r = map(int, input().split())
    steps = [1]
    mods = [1]
    ans = [1]
    mod = 1
    get_ans(n)
    mods.append(0)
    if n > 0:
        print(get(r) - get(l - 1))
    else:
        print(0)