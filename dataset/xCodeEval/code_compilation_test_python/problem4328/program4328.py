def get_ans(n, k):
        
        global fact
        global ans
        a = []
        
        if (n <= 0):
            return a
       
        curnum = 1
        curl = 0
        curr = ans[n - 1] - 1
        while (1 == 1):
            if ((curl <= k) and (curr >= k)):
                break
            curnum += 1
            curl = curr + 1
            curr = curl + ans[n - curnum] * fact[curnum - 2] - 1
        a.append(curnum)
        
        if (curnum == 1):
            l = get_ans(n - 1, k)
            a.extend(l)
            return a
    
        k1 = k - curl
        k1 = k // ans[n - curnum]
        pos = 2
        used = [-1] * curnum
        used[curnum - 1] = 0
        for i in range(2, curnum):
            poss = []
            for j in range(curnum):
                if (used[j] != -1):
                    continue
                if (j + 1 == pos):
                    continue
                if (j == used[pos - 1]):
                    continue
                poss.append(j + 1)
            cnum = k1 // fact[curnum - i - 1]
            a.append(cnum + 1)
            k1 = k1 % fact[curnum - i - 1]
            used[cnum] = pos - 1
            pos += 1
        for i in range(curnum):
            if (used[i] == -1):
                a.append(i + 1)
                break
        l = get_ans(n - curnum, k % ans[n - curnum])
        a.extend(l)
        return a
    
          
    
    n, k = list(map(int, input().rstrip().split()))
    
    
    fact = []
    fact.append(1)
    for i in range(1, 51):
        fact.append(fact[i - 1] * i)
    
    ans = []
    ans.append(1)
    ans.append(1)
    
    for i in range(2, 51):
        ans.append(0)
        for j in range(1, i + 1):
            if (j == 1):
                ans[i] += ans[i - 1]
                continue
            ans[i] += ans[i - j] * fact[j - 2]
    
    a = []
    
    a = get_ans(n, k - 1)
    i = 0
    csum = 0
    while i < n:
        sz = a[i]
        for j in range(sz):
            a[i] += csum
            i += 1
        csum += sz
    
    for i in range(n):
        print(a[i], ' ', sep = '', end = '')
    print()