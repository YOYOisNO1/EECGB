def program3817():
    for _ in range(int(input())):
        a, b, m = [int(i) for i in input().split()]
    
        if a == b:
            print("1 " + str(a))
            continue
    
        l = a + 1
        r = a + m
        cnt = 1
        while r < b:
            l += l
            r += r
            cnt += 1
    
        if l > b:
            print(-1)
            continue
    
        ls = [1] * cnt
        p2 = [2 ** (cnt - 2 - i) for i in range(cnt - 1)] + [1]
        for i in range(cnt):
            while ls[i] < m and l + p2[i] <= b:
                ls[i] += 1
                l += p2[i]
    
        ans = [a]
        ps = a
        for i in ls:
            a = ps + i
            ps += a
            ans += [a]
    
        print(str(cnt + 1) + " " + ' '.join(str(i) for i in ans))